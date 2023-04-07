# panel de administrador de proyectos/aplicaciones 'predeterminado' (crear: datos, usuarios, roles)

# ----- ARCHIVO ORIGINAL CREADO POR STARTAPP DJANGO ------------------

from django.contrib import admin
# Register your models here.

# puedo importar los modelos/clases/tablas que ya hice en la carpeta modelos
from .models import tabla_proyectos, tabla_tareas

# y puedo agregarlos al panel de control por defecto:
admin.site.register(tabla_proyectos)
admin.site.register(tabla_tareas)

