from django.db import models

# Create your models here.
class BodegaProveedor(models.Model):
    # Atributos del modelo
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    # Otros campos y relaciones

class BodegaPrincipal(models.Model):
    # Atributos del modelo
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    # Otros campos y relaciones

class Cliente(models.Model):
    # Atributos del modelo
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    # Otros campos y relaciones

class Cilindro(models.Model):
    # Atributos del modelo
    codigo = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    # Otros campos y relaciones