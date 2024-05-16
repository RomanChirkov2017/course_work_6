from django.conf import settings
from django.db import models
from django.utils import timezone

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    email = models.EmailField(max_length=150, unique=True, verbose_name='Email')
    FIO = models.CharField(max_length=250, verbose_name='ФИО')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)
    avatar = models.ImageField(upload_to='mailings/', **NULLABLE, verbose_name='Аватар')
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='Пользователь'
    )

    def __str__(self):
        return f"{self.email} - {self.FIO}"

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('FIO',)


class Message(models.Model):
    title = models.CharField(max_length=250, verbose_name='Тема письма')
    text = models.TextField(verbose_name='Текст письма')
    image = models.ImageField(upload_to='mailings/', **NULLABLE, verbose_name='Изображение')
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='Пользователь'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class MailingSettings(models.Model):
    DAILY = "Раз в день"
    WEEKLY = "Раз в неделю"
    MONTHLY = "Раз в месяц"

    PERIODICITY_CHOICES = [
        (DAILY, "Раз в день"),
        (WEEKLY, "Раз в неделю"),
        (MONTHLY, "Раз в месяц"),
    ]

    CREATED = "Создана"
    STARTED = "Запущена"
    COMPLETED = "Завершена"

    STATUS_CHOICES = [
        (CREATED, "Создана"),
        (STARTED, "Запущена"),
        (COMPLETED, "Завершена"),
    ]

    title = models.CharField(max_length=250, **NULLABLE, verbose_name='Тема рассылки')
    start_time = models.DateTimeField(default=timezone.now, verbose_name='Время начала рассылки')
    end_time = models.DateTimeField(default=timezone.now, verbose_name='Время окончания рассылки')
    last_send = models.DateTimeField(**NULLABLE, verbose_name='Дата последней отправки')
    periodicity = models.CharField(max_length=50, choices=PERIODICITY_CHOICES, verbose_name='Периодичность')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=CREATED, verbose_name='Статус рассылки')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='Владелец рассылки')
    clients = models.ManyToManyField(Client, verbose_name='Клиенты')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщения')
    is_active = models.BooleanField(default=True, verbose_name='Активна/Неактивна')

    def __str__(self):
        return f"time: {self.start_time} - {self.end_time}, periodicity: {self.periodicity}, status: {self.status}"

    class Meta:
        verbose_name = 'Настройка рассылки'
        verbose_name_plural = 'Настройки рассылки'
        permissions = [
            ('view_any_mailings', 'Can view any mailings'),
            ('change_mailing_is_active', 'Can change mailing is active'),
        ]


class Log(models.Model):
    time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки')
    status = models.BooleanField(verbose_name='Статус попытки')
    server_answer = models.CharField(**NULLABLE, verbose_name='Ответ почтового сервера')
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='Пользователь'
    )

    mailing_list = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='Рассылка')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Клиент')

    def __str__(self):
        return f"{self.time}: {self.status}"

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
