from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'