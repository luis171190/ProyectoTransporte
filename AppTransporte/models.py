from django.db import models

# Create your models here.


class Pasajero(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    numeroDeDocumento = models.IntegerField()
    vacunado = models.BooleanField()

class Chofer(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    numeroDeDocumento = models.IntegerField()
    numeroDeLicencia = models.IntegerField()

class Transporte(models.Model):
    tipo = models.CharField(max_length=40) #Tipo: Aereo o terrestre
    empresa = models.CharField(max_length=40) #Empresa a cargo
    capacidad = models.IntegerField() #Capacidad del transporte
    patente = models.IntegerField()

class Terminal(models.Model):
    nombre = models.CharField(max_length=40)
    ubicacion = models.CharField(max_length=40)
    

