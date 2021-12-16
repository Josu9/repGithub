from django.contrib import admin

from .models import Bibliotecas, Libros, Asociados
# Register your models here.

admin.site.register(Bibliotecas)
admin.site.register(Libros)
admin.site.register(Asociados)