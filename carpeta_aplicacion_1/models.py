# crear clases / tablas sql con ayuda del ORM en archivos migrations en carpeta migrations

# ----- ARCHIVO ORIGINAL CREADO POR STARTAPP DJANGO ------------------

from django.db import models

# Create your models here.

# se crea una clase, que tiene parámetros/hereda los modelos de djando, que asu vez llama la clase model
# esta ya es una tabla/clase/modelo con 2 columnas (id, nombre)
class clase_proyectos (models.Model):
    # SQL permite especificar el tipo de dato
    nombre_clase_proyectos = models.CharField(max_length=200)

class clase_tareas (models.Model):
    titulo_clase_tareas = models.CharField(max_length=200)
    descripcion_clase_tareas = models.TextField()
    # foreignkey = esta tabla tiene relacion con otra tabla y lo relaciona con ids
    # 'on_delete=models.CASCADE': cuando se elimine un elemento de la tabla asociada, se elimina todas las tareas de esa tabla asociada
    n_proyecto_clase_tareas = models.ForeignKey(clase_proyectos,on_delete=models.CASCADE)
