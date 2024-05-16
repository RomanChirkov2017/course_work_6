from django.conf import settings
from django.core.mail import send_mail


def send_mailing(message, mail_settings):
    print(message.title, message.text)
    print([client.email for client in mail_settings.clients.all()])
    send_mail(
        subject=message.title,
        message=message.text,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[client.email for client in mail_settings.clients.all()],
        fail_silently=False
    )

