# Generated by Django 4.2 on 2024-04-23 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0004_alter_mailingsettings_clients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingsettings',
            name='clients',
            field=models.ManyToManyField(to='mailings.client', verbose_name='Клиенты'),
        ),
    ]
