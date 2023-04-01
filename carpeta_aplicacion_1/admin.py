# panel de administrador de proyectos/aplicaciones 'predeterminado' (crear: datos, usuarios, roles)

# ----- ARCHIVO ORIGINAL CREADO POR STARTAPP DJANGO ------------------

from django.contrib import admin
# Register your models here.

# puedo importar los modelos/clases/tablas que ya hice en la carpeta modelos
from .models import clase_proyectos, clase_tareas

# y puedo agregarlos al panel de control por defecto:
admin.site.register(clase_proyectos)
admin.site.register(clase_tareas)

