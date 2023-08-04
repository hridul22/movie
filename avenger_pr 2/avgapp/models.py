from django.db import models

# Create your models here.


class Avenger(models.Model):

    name = models.CharField(max_length=252)
    decs = models.TextField()
    img = models.ImageField(upload_to='gallery')


def __str__(self):
   return self.name
