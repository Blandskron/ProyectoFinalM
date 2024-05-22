from django.urls import path
from . import views

urlpatterns = [
    path('listar_libros/', views.listar_libros, name='listar_libros'),
    path('crear_libro/', views.crear_libro, name='crear_libro'),
    path('actualizar_libro/<int:id>/', views.actualizar_libro, name='actualizar_libro'),
    path('eliminar_libro/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
]
