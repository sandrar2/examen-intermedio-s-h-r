from django.db import models

# Create your models here.

class Meseros(models.Model):
    nombre = models.CharField(max_length=25)
    edad = models.IntegerField(default='00')
    nacionalidad = models.CharField(max_length=27, default='')
    dni = models.IntegerField(default='00000000')


