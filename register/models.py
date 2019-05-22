from django.db import models
from django.urls import reverse


# Create your models here.
class Register(models.Model):
    name_lost = models.CharField(max_length=50)
    location_lost = models.CharField(max_length=50)
    gender_lost = models.CharField(max_length=50)
    image_lost = models.FileField()

    def get_absolute_url(self):
        return reverse('register:register')

    def __str__(self):
        return self.name_lost
