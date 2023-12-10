from django.db import models
from django.db.models import Model

# Create your models here.

class Servicios(Model):
    nombre_tratamiento = models.CharField(max_length=50, default="tratamiento x")
    cantidad_sesiones = models.PositiveIntegerField(default=1)
    precio_sugerido = models.FloatField(default=10000)
    email = models.EmailField(max_length=50, null=False, blank= False, default="email@mail.com")
    fecha = models.DateField(blank=False, null=False, auto_now=True)

class Meta:
    db_table = "Nuevos_tratamientos"

def __str__(self):
    return f"El nombre del tratamiento sugerido es: {self.nombre_tratamiento} y tendrá {self.cantidad_sesiones} sesiones"

