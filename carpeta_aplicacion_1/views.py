# define que envia al cliente/navegador para ver en pantalla (archivos html)
# ----- ARCHIVO ORIGINAL CREADO POR STARTAPP DJANGO ------------------

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# funcion convencional con parámetro enviar repuesta HTTP
# va a retornar HttpResponse, cuando se ejecute va a devolver al navegador
# var var_params_ruta es una variable dentro de la ruta y debe tener el mismo nombre para su referencia

def view_funcion_hello(view_funcion_hello_param_request, var_params_ruta):
    return HttpResponse('texto: hola isaac')

def view_funcion_acerca_de(view_funcion_acerca_param_request):
    return HttpResponse('texto: acerca de')

def view_funcion_index(view_funcion_index_param_request):
    return HttpResponse('texto: index')

