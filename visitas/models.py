from django.db import models

# Create your models here.
class Visita(models.Model):
    cliente = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    tipo_servicio = models.CharField(max_length=200)
    disponibilidad = models.CharField(max_length=200)
    tipo_servicio = models.CharField(max_length=200)
    fecha = models.DateField()
    estado = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('Realizada', 'Realizada'), ('Cancelada', 'Cancelada')], default='Pendiente')
    metros_cuadrados = models.FloatField()

    def __str__(self):
        return f"Visita a {self.cliente} el {self.fecha} a las {self.hora}"