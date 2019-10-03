from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    idCard = models.CharField(max_length=10, blank=True, default='')
    birthday = models.DateField()
    career = models.CharField(max_length=100, blank=True, default='')

