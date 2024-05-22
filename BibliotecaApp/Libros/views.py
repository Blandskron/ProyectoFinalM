from django.shortcuts import render, redirect
from .models import Libro, Autor
from .forms import LibroForm, AutorForm

# CREATE
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'Libros/crear_libro.html', {'form': form})

# READ
def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'Libros/listar_libros.html', {'libros': libros})

# UPDATE
def actualizar_libro(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == 'GET':
        form = LibroForm(instance=libro)
    else:
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    return render(request, 'Libros/actualizar_libro.html', {'form': form})


# DELETE
def eliminar_libro(request, id):
  libro = Libro.objects.get(id=id)
  libro.delete()
  return redirect('listar_libros')


# ORM CONSULTA SQL

