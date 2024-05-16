# Generated by Django 4.2 on 2024-05-14 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350, verbose_name='Заголовок')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Содержимое статьи')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Изображение')),
                ('view_count', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('publish_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('is_published', models.BooleanField(default=True, verbose_name='Признак публикации')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]