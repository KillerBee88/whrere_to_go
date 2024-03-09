from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Заголовок')
    short_description = models.TextField(
        null=False, blank=True, verbose_name='Краткое описание')
    long_description = HTMLField(
        null=False, blank=True, verbose_name='Полное описание')
    latitude = models.FloatField(
        null=False, blank=False, verbose_name='Широта')
    longitude = models.FloatField(
        null=False, blank=False, verbose_name='Долгота')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title

    def get_coordinates(self):
        return [self.latitude, self.longitude]


class Image(models.Model):
    location = models.ForeignKey(
        Place, related_name='images', on_delete=models.CASCADE, verbose_name='Местоположение')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    order = models.IntegerField(default=0, verbose_name='Порядок', db_index=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f"{self.order}: {self.image.url}"
