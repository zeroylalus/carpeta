# define que envia al cliente/navegador para ver en pantalla (archivos html)

# ----- ARCHIVO ORIGINAL CREADO POR STARTAPP DJANGO ------------------

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# funcion convencional con parámetro enviar repuesta HTTP
def view_fun_hello(view_fun_hello_param_request):
    # va a retornar HttpResponse, cuando se ejecute va a devolver al navegador
    return HttpResponse('texto: hola isaac')

def view_fun_acerca_de(view_fun_acerca_param_request):
    return HttpResponse('texto: acerca de')

