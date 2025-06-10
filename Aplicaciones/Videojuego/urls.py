from django.urls import path
from . import views

urlpatterns = [
    path('listaVideojuegos/', views.listaVideojuegos, name='listaVideojuegos'),
    path('listaVideojuegos/nuevoVideojuego/', views.nuevoVideojuego, name='nuevoVideojuego'),
    path('guardarVideojuego/', views.guardarVideojuego, name='guardarVideojuego'),
    path('eliminarVideojuego/<int:id>/', views.eliminarVideojuego, name='eliminarVideojuego'),
    path('editarVideojuego/<int:id>/', views.editarVideojuego, name='editarVideojuego'),
    path('procesarEdicionVideojuego/', views.procesarEdicionVideojuego, name='procesarEdicionVideojuego'),
]
