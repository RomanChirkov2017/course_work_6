# Generated by Django 4.2 on 2024-04-30 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0011_alter_mailingsettings_last_send'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailingsettings',
            name='message',
        ),
        migrations.AddField(
            model_name='mailingsettings',
            name='message',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mailings.message', verbose_name='Сообщения'),
            preserve_default=False,
        ),
    ]