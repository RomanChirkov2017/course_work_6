# Generated by Django 4.2 on 2024-04-24 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0005_alter_mailingsettings_clients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingsettings',
            name='end_time',
            field=models.TimeField(verbose_name='Время окончания рассылки'),
        ),
        migrations.AlterField(
            model_name='mailingsettings',
            name='start_time',
            field=models.TimeField(verbose_name='Время начала рассылки'),
        ),
    ]
