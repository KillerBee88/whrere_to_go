from django.db import models
from tinymce.models import HTMLField

class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description_short = models.TextField(null=True, blank=True, verbose_name='Краткое описание')
    description_long = HTMLField(null=True, blank=True, verbose_name='Полное описание')
    latitude = models.FloatField(null=True, blank=True, verbose_name='Широта')
    longitude = models.FloatField(null=True, blank=True, verbose_name='Долгота')

    def get_coordinates(self):
        return [self.latitude, self.longitude]

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

class Image(models.Model):
    location = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE, verbose_name='Местоположение')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    order = models.IntegerField(default=0, verbose_name='Порядок')

    def __str__(self):
        return f"{self.order}: {self.image.url}"

    class Meta:
        ordering = ['order']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'