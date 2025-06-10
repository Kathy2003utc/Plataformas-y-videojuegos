from django.db import models
from Aplicaciones.Plataforma.models import Plataforma

class Videojuego(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField()
    plataforma_principal = models.ForeignKey(Plataforma, on_delete=models.CASCADE, related_name='Plataforma')
    def __str__(self):
        return self.titulo