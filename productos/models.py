from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator


# Create your models here.

class Producto(models.Model):
    class Tipo(models.TextChoices):
        TELEVISOR = "TELEVISOR","Televisor"
        LAPTOP = "LAPTOP", "Laptop"
        ZAPATO = "ZAPATO", "Zapato"



    nombre = models.CharField(max_length=50)
    sku = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    marca = models.CharField(max_length=30)
    costo = models.FloatField(validators=[MinValueValidator(0.0)])

    tipo_producto = models.CharField(max_length=20,choices=Tipo.choices,default=Tipo.TELEVISOR)

    class Meta:
        abstract = True

    
    def obtener_precio_venta(self,porcentaje_utilidad):
        return self.costo /(1 - porcentaje_utilidad)

    def __str__(self):
        return self.nombre
    

class Televisor(Producto):
    tipo_pantalla = models.CharField(max_length=20)
    tamano_pantalla = models.IntegerField(validators=[MinValueValidator(0)])
    tipo_producto = Producto.Tipo.TELEVISOR

    porcentaje_utilidad = 0.35


class Laptop(Producto):
    procesador = models.CharField(max_length=20)
    memoria_ram = models.IntegerField(validators=[MinValueValidator(0)])
    tipo_producto = Producto.Tipo.LAPTOP

    porcentaje_utilidad = 0.40



class Zapato(Producto):
    material = models.CharField(max_length=20)
    numero = models.IntegerField(validators=[MinValueValidator(0)])
    tipo_producto = Producto.Tipo.ZAPATO

    porcentaje_utilidad = 0.30



