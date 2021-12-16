from django.urls import path
from App1 import views

urlpatterns = [
    
<<<<<<< HEAD
 path('inicio', views.inicio, name="Inicio"),
 path('bibliotecas', views.bibliotecas, name="Bibliotecas"),
 path('libros', views.libros, name="Libros"),
 path('asociados', views.asociados, name="Asociados"),
 path('bibliotecasFormulario', views.bibliotecasFormulario, name="BibliotecasFormulario"),
 path('librosFormulario', views.librosFormulario, name="LibrosFormulario"),   
 path('asociadosFormulario', views.asociadosFormulario, name="AsociadosFormulario"),   
=======
 path('inicio',views.inicio, name = "Inicio"),
 path('bibliotecas',views.bibliotecas, name = "Bibliotecas"),
 path('libros',views.libros, name = "Libros"),
 path('asociados',views.asociados, name = "Asociados"),
>>>>>>> 415ca0f6f6a05799160d02afd0d264db48157be1
    
]