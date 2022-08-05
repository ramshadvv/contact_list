from django.db import models

# Create your models here.
class contactlist(models.Model):
    name = models.CharField(max_length=255)
    Phone_number = models.IntegerField()