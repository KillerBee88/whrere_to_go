from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

class Image(models.Model):
    location = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'