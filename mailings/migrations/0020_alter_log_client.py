# Generated by Django 4.2 on 2024-05-05 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0019_mailingsettings_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mailings.client', verbose_name='Клиент'),
        ),
    ]