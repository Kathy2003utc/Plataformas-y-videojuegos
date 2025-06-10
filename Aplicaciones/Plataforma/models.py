from django.db import models

class Plataforma(models.Model):
    nombre = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)
    lanzamiento = models.DateField()
    version_sistema = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
