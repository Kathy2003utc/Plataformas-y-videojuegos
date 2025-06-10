from django.shortcuts import render, redirect
from .models import Videojuego, Plataforma
from django.contrib import messages

# Listar videojuegos
def listaVideojuegos(request):
    videojuegoListado = Videojuego.objects.all()
    return render(request, "listaVideojuegos.html", {'Videojuego': videojuegoListado})

# Mostrar formulario para nuevo videojuego
def nuevoVideojuego(request):
    plataformas = Plataforma.objects.all()
    return render(request, "nuevoVideojuegos.html", {'plataformas': plataformas})

# Guardar videojuego nuevo
def guardarVideojuego(request):
    titulo = request.POST['titulo']
    genero = request.POST['genero']
    fecha_lanzamiento = request.POST['fecha_lanzamiento']
    plataforma_id = request.POST['plataforma_principal']

    plataforma = Plataforma.objects.get(id=plataforma_id)

    Videojuego.objects.create(
        titulo=titulo,
        genero=genero,
        fecha_lanzamiento=fecha_lanzamiento,
        plataforma_principal=plataforma
    )
    messages.success(request, "Videojuego guardado exitosamente")
    return redirect('/listaVideojuegos/')

# Eliminar videojuego
def eliminarVideojuego(request, id):
    videojuegoEliminar = Videojuego.objects.get(id=id)
    videojuegoEliminar.delete()
    messages.success(request, "Videojuego eliminado exitosamente")
    return redirect('/listaVideojuegos/')

# Mostrar formulario para editar videojuego
def editarVideojuego(request, id):
    videojuegoEditar = Videojuego.objects.get(id=id)
    plataformas = Plataforma.objects.all()
    return render(request, "editarVideojuegos.html", {
        'videojuegoEditar': videojuegoEditar,
        'plataformas': plataformas
    })

# Procesar edición de videojuego
def procesarEdicionVideojuego(request):
    id = request.POST["id"]
    titulo = request.POST["titulo"]
    genero = request.POST["genero"]
    fecha_lanzamiento = request.POST["fecha_lanzamiento"]
    plataforma_id = request.POST["plataforma_principal"]

    videojuego = Videojuego.objects.get(id=id)
    plataforma = Plataforma.objects.get(id=plataforma_id)

    videojuego.titulo = titulo
    videojuego.genero = genero
    videojuego.fecha_lanzamiento = fecha_lanzamiento
    videojuego.plataforma_principal = plataforma

    videojuego.save()
    messages.success(request, "Videojuego actualizado exitosamente")
    return redirect('/listaVideojuegos/')
