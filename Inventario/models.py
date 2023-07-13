from django.db import models

# Create your models here.
class libro(models.Model):
    nombre_libro=models.CharField(max_length=20)
    nombre_autor=models.CharField(max_length=20)
    categoria=models.CharField(max_length=20)
    Precio=models.FloatField()
    codigo=models.CharField(max_length=20)
    estado=models.CharField(max_length=2)
    def __str__(self):
        return 'libro: {self.nombre_libro}'    