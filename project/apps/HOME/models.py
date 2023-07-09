from django.db import models

# Create your models here.
class BodegaProveedor(models.Model):
    # Atributos del modelo
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    # Otros campos y relaciones

    def __str__(self):
        return self.nombre
    
class BodegaPrincipal(models.Model):
    # Atributos del modelo
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    # Otros campos y relaciones

    def __str__(self):
        return self.nombre
class Cliente(models.Model):
    # Atributos del modelo
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    # Otros campos y relaciones
    def __str__(self):
        return self.nombre
class Cilindro(models.Model):
    # Atributos del modelo
    codigo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    # Otros campos y relaciones

    def __str__(self):
        return self.codigo