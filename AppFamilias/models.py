from django.db import models

# Create your models here.

class Familiar1(models.Model):
    nombre_apellido=models.CharField(max_length=50)
    nacimiento=models.IntegerField()
    dni=models.IntegerField()

class Familiar2(models.Model):
    nombre_apellido=models.CharField(max_length=50)
    nacimiento=models.IntegerField()
    dni=models.IntegerField()

class Familiar3(models.Model):
    nombre_apellido=models.CharField(max_length=50)
    nacimiento=models.IntegerField()
    dni=models.IntegerField()





