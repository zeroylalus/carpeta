""" ARCHIVO ORIGINAL CREADO POR STARTAPP DJANGO:
. define que envia al cliente/navegador para ver en pantalla (archivos html)

"""

from django.shortcuts import render
# Jasonresponse, formato q entiende navegador, representar conjunto elementos (queryset)
# ctrl + space : mostrar sugerencias
from django.http import HttpResponse, JsonResponse
from .models import clase_proyectos, clase_tareas
from django.shortcuts import get_object_or_404

# Create your views here.

"""
. funcion convencional con parámetro que envía repuesta HTTP
. función retorna HttpResponse, y cuando ejecute devuelve al navegador ('texto: hola isaac')
. var var_params_ruta es una variable dentro de la ruta y debe tener el mismo nombre para su referencia
. %s concatena un texto con una variante (crea un parametro que ira cambiando conforme cambio de una url a otra)
"""

# --> funciones de ejemplo:

def view_funcion_hello_str(view_funcion_hello_param_request, var_params_ruta):
    print(type(var_params_ruta))
    return HttpResponse("texto: " + var_params_ruta)

def view_funcion_hello_int(view_funcion_hello_int_param_request, var_params_ruta_int):
    return HttpResponse("<h1>texto: la ruta entero dice '%s'<h1>" % var_params_ruta_int)

# --> funciones de datos:

def view_funcion_acerca_de(view_funcion_acerca_param_request):
    return HttpResponse('texto: acerca de')

def view_funcion_index(view_funcion_index_param_request):
    return HttpResponse('texto: index')

# --> funciones que mostrarán y obtendran datos de proyectos y tareas

def view_funcion_proyectos(view_funcion_proyectos_param_request):
    # buscar, enviar, mostrar, etc. datos de database (atraves de parámetros)
    # el query set para ser visualizado debe convertirse en lista y establecer el parametro "safe" a False
    # .all() todos los "datos" y .values() solo los valores
    queryset_proyectos = list(clase_proyectos.objects.values())
    return JsonResponse(queryset_proyectos, safe=False)

def view_funcion_tareas(view_funcion_tareas_param_request, var_url_id):
    #nota: como el get_object_or_404 remplaza el buscar el objeto especificando el modelo/clase/tabla
    #var_get_titulo_tarea = clase_tareas.objects.get(id = var_url_id)
    # el espacio se cambia a %20 por que hace un encode, esta codificando la url
    # antes de usar render hemos solo devuelto strings
    var_get_titulo_tarea = get_object_or_404(clase_tareas, id = var_url_id)
    return HttpResponse('texto: el titulo de la tarea del id en la ruta es = "%s"' % var_get_titulo_tarea.titulo_clase_tareas)

