# Generated by Django 4.2 on 2024-05-02 08:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0014_alter_mailingsettings_last_send'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingsettings',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время окончания рассылки'),
        ),
        migrations.AlterField(
            model_name='mailingsettings',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время начала рассылки'),
        ),
    ]
