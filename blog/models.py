from django.db import models

from mailings.models import NULLABLE


class Blog(models.Model):
    title = models.CharField(max_length=350, verbose_name='Заголовок')
    content = models.TextField(**NULLABLE, verbose_name='Содержимое статьи')
    image = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='Изображение')
    view_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')

    def __str__(self):
        return f'{self.title} ({self.publish_date})'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
