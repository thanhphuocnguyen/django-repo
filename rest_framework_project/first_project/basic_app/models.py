from django.db import models


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    model = models.CharField(max_length=255)

    def __str__(self):
        return self.name
