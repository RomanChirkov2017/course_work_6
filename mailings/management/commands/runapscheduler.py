import logging
import smtplib
from datetime import datetime, timedelta

import pytz
from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

from mailings.models import MailingSettings, Log
from mailings.services import send_mailing

logger = logging.getLogger(__name__)


def my_job():
    naive_datetime = datetime.now()
    now = naive_datetime.replace(tzinfo=pytz.utc)
    mailings = MailingSettings.objects.all()
    for mailing in mailings:
        start_time = mailing.start_time
        end_time = mailing.end_time
        message = mailing.message
        if start_time < now < end_time:
            mailing.status = "Запущена"
            try:
                send_mailing(message, mailing)
                mailing.last_send = now
                mailing.status = "Завершена"
                if mailing.periodicity == "Раз в день":
                    mailing.start_time += timedelta(days=1, hours=0, minutes=0)
                    mailing.end_time += timedelta(days=1, hours=0, minutes=0)
                elif mailing.periodicity == "Раз в неделю":
                    mailing.start_time += timedelta(days=7, hours=0, minutes=0)
                    mailing.end_time += timedelta(days=7, hours=0, minutes=0)
                elif mailing.periodicity == "Раз в месяц":
                    mailing.start_time += timedelta(days=30, hours=0, minutes=0)
                    mailing.end_time += timedelta(days=30, hours=0, minutes=0)
                print('Рассылка успешно отправлена!')
                Log.objects.create(status=True, mailing_list=mailing)
            except smtplib.SMTPException as e:
                print('Ошибка отправки рассылки')
                Log.objects.create(status=False, mailing_list=mailing, server_answer=e)

        mailing.save()


@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    This job deletes APScheduler job execution entries older than `max_age` from the database.
    It helps to prevent the database from filling up with old historical records that are no
    longer useful.

    :param max_age: The maximum length of time to retain historical job execution records.
                    Defaults to 7 days.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(second="*/10"),  # Every 10 seconds
            id="my_job",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Midnight on Monday, before start of the next work week.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
