from django.db import models

# Create your models here.

class Pacientes(models.Model):
    id = models.CharField(primary_key=True,max_length=6)
    nombre= models.CharField(max_length=50)
    tratamiento= models.CharField(max_length=50)
    precio= models.CharField(max_length=10)
    telefono= models.CharField(max_length=15)
    fecha=models.CharField(max_length=12)

def __str__(self):
    texto = "{0} ({1})"
    return texto.format(self.nombre, self.id)
