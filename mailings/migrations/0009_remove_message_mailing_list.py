# Generated by Django 4.2 on 2024-04-26 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0008_client_avatar_message_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='mailing_list',
        ),
    ]