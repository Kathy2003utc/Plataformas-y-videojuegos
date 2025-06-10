from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Plataforma
from django.contrib import messages

# Listar plataformas
def listaPlataformas(request):
    plataformaListado = Plataforma.objects.all()
    return render(request, "listaPlataforma.html", {'Plataforma': plataformaListado})

# Mostrar formulario para nueva plataforma
def nuevaPlataforma(request):
    return render(request, "nuevaPlataforma.html")

# Guardar plataforma nueva
def guardarPlataforma(request):
    nombre = request.POST['nombre']
    fabricante = request.POST['fabricante']
    lanzamiento = request.POST['lanzamiento']
    version_sistema = request.POST['version_sistema']

    Plataforma.objects.create(
        nombre=nombre,
        fabricante=fabricante,
        lanzamiento=lanzamiento,
        version_sistema=version_sistema
    )
    messages.success(request, "Plataforma guardada exitosamente")
    return redirect('/listaPlataformas/')

# Eliminar plataforma
def eliminarPlataforma(request, id):
    plataformaEliminar = Plataforma.objects.get(id=id)
    plataformaEliminar.delete()
    messages.success(request, "Plataforma eliminada exitosamente")
    return redirect('/listaPlataformas/')

# Mostrar formulario para editar plataforma
def editarPlataforma(request, id):
    plataformaEditar = Plataforma.objects.get(id=id)
    return render(request, "editarPlataforma.html", {
        'plataformaEditar': plataformaEditar
    })

# Procesar edición de plataforma
def procesarEdicionPlataforma(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    fabricante = request.POST["fabricante"]
    lanzamiento = request.POST["lanzamiento"]
    version_sistema = request.POST["version_sistema"]

    plataforma = Plataforma.objects.get(id=id)
    plataforma.nombre = nombre
    plataforma.fabricante = fabricante
    plataforma.lanzamiento = lanzamiento
    plataforma.version_sistema = version_sistema

    plataforma.save()
    messages.success(request, "Plataforma actualizada exitosamente")
    return redirect('/listaPlataformas/')
