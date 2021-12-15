from django.db import models


class Biblioteca (models.Model):
     ubicacion = models.CharField(max_length=60)
     nroAsociados = models.IntegerField()

class Libros (models.Model):
    genero = models.CharField(max_length=40)
    nombre = models.CharField(max_length=50)
    numeroId = models.IntegerField()

class Asociados (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nroCarnet = models.IntegerField()
    email = models.EmailField()
