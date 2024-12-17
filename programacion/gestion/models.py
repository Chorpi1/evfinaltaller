from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio_unitario = models.IntegerField()
    fecha_vencimiento = models.DateField()
    stock = models.PositiveIntegerField()
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


