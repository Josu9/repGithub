from django.urls import path
from App1 import views

urlpatterns = [
    
 path('inicio',views.inicio),
 path('bibliotecas',views.bibliotecas),
    
]