from django.contrib import admin

from .models import Bibliotecas, Libros, Asociados
# Register your models here.

<<<<<<< HEAD
from .models import *

admin.site.register(Bibliotecas)

admin.site.register(Libros)

=======
admin.site.register(Bibliotecas)
admin.site.register(Libros)
>>>>>>> 415ca0f6f6a05799160d02afd0d264db48157be1
admin.site.register(Asociados)