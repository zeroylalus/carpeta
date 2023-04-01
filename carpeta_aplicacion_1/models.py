""" ARCHIVO ORIGINAL CREADO POR STARTAPP DJANGO:
crear clases / tablas sql con ayuda del ORM en archivos migrations en carpeta migrations
"""

from django.db import models

# Create your models here.

""" ---> NOTAS: 
. se crea clase tiene parámetros/hereda modelos de djando, que llama a clase model
. ya es tabla/clase/modelo con 2 columnas (id, nombre)
. SQL permite especificar el tipo de dato
. __str__ metodo/función permite mostrar algo a la interfaz """
class clase_proyectos (models.Model):
    nombre_clase_proyectos = models.CharField(max_length=200)
    def __str__ (self_proyecto):
        return self_proyecto.nombre_clase_proyectos

"""---> NOTAS:
. foreignkey = esta tabla tiene relacion con otra tabla y lo relaciona con ids
. 'on_delete = models.CASCADE': si se elimine elemento de tabla asociada, se elimina todos los elementos de esta tabla """
class clase_tareas (models.Model):
    titulo_clase_tareas = models.CharField(max_length=200)
    descripcion_clase_tareas = models.TextField()
    n_proyecto_clase_tareas = models.ForeignKey(clase_proyectos,on_delete=models.CASCADE)
    def __str__ (self_tarea):
        return self_tarea.titulo_clase_tareas + ' - ' + self_tarea.n_proyecto_clase_tareas.nombre_clase_proyectos
