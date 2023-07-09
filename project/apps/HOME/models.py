from django.db import models


class Cilindro(models.Model):
    # Atributos del modelo
    codigo = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    

    def __str__(self):
        return self.codigo
# Create your models here.
class BodegaProveedor(models.Model):
    # Atributos del modelo
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    codigo_cilindro = models.ForeignKey(Cilindro, on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return self.nombre
    
class BodegaPrincipal(models.Model):
    # Atributos del modelo
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    codigo_cilindro = models.ForeignKey(Cilindro, on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return self.nombre
class Cliente(models.Model):
    # Atributos del modelo
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    codigo_cilindro = models.ForeignKey(Cilindro, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.nombre
 