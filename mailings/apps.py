from time import sleep

from django.apps import AppConfig
from django.core.management import call_command

class MailingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailings'

    #def ready(self):
    #    call_command('runapscheduler')
