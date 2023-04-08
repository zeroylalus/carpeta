""" ARCHIVO ORIGINAL CREADO POR STARTAPP DJANGO:
. RELACIÓN: MODELOS, VAR URLS, DICCIONARIOS TEMPLETES
. define que envia al cliente/navegador para ver en pantalla (archivos html)

"""

# Jasonresponse, formato q entiende navegador, representar conjunto elementos (queryset)
# ctrl + space : mostrar sugerencias
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import tabla_proyectos, tabla_tareas
from .formularios import tabla_crear_tarea, tabla_crear_proyecto

# Create your views here.

"""
. funcion convencional con parámetro que envía repuesta HTTP
. función retorna HttpResponse, y cuando ejecute devuelve al navegador ('texto: hola isaac')
. var var_params_ruta es una variable dentro de la ruta y debe tener el mismo nombre para su referencia
. %s concatena un texto con una variante (crea un parametro que ira cambiando conforme cambio de una url a otra)
. HttpResponse devuelve strings (etiquetas, archivos,templates: html) q navegador interpreta
. HttpResponse sirve para probar una respuesta sencilla al cliente
"""

# --> funciones de ejemplo:

def view_funcion_hello_str(view_funcion_hello_param_request, var_params_ruta):
    print(type(var_params_ruta))
    return HttpResponse("texto: " + var_params_ruta)

def view_funcion_hello_int(view_funcion_hello_int_param_request, var_params_ruta_int):
    return HttpResponse("<h1>texto: la ruta entero dice '%s'<h1>" % var_params_ruta_int)

# --> funciones de datos:

# pasar variable var_titulo al segundo parametro de render para visualizarlo en alguna parte del archivo html, no es necesario procesar el archivo html o leerlo con modulos del sistema o modulos de lectura de archivos de python, ya viene integrado en django, atravez del 3er parametro en forma de 'diccionario: pares de clave/valor' y declarando ''diccionario_titulo': var_titulo', el archivo html ya tiene referencia clave = referencia al html / valor = variable en este caso (pueden ser string, int, boolean), diccinarios y listas los transforma a strings, ya que html solo espera texto y lo procesa, poir lo tanto la lista de proyectos quedaria mal

def view_funcion_index(view_funcion_index_param_request):
    var_titulo = 'bienvenido al curso'
    return render(view_funcion_index_param_request, 'index.html',{
        'ref_html_titulo': var_titulo
    })

def view_funcion_acerca_de(view_funcion_acerca_param_request):
    var_usuario = 'USUARIO: ISAAC'
    return render(view_funcion_acerca_param_request, 'acerca de.html',{
        'ref_html_usuario': var_usuario
    })

# --> funciones que mostrarán y obtendran datos de proyectos y tareas

"""
. queryset para ser visto debe convertirse en lista y establecer el parametro "safe" a False
. El clase .all() todos los "datos" y .values() solo los valores
. queryset_proyectos = list(clase_proyectos.objects.values())
. funcionalidad template engine 'for': de 'listas' generar multiples elementos, lista ul, multiples tarjetas, etc. /interpretar código a modo de condicionales
"""

def view_funcion_proyectos(view_funcion_proyectos_param_request):
    queryset_proyectos = tabla_proyectos.objects.all()
    return render(view_funcion_proyectos_param_request, 'proyectos/proyectos.html',{
        'ref_html_proyectos': queryset_proyectos
    })

"""
. como el get_object_or_404 remplaza el buscar el objeto especificando el modelo
. var_get_titulo_tarea = tabla_tareas.objects.get(id = var_url_id)
. en la ruta el espacio se cambia a %20 por que hace un encode, esta codificando la url
. antes de usar render solo hemos devuelto strings copn httpresponse
. buscar, enviar, mostrar, etc. datos de database con params, vars en ruta
. def view_funcion_tareas(view_funcion_tareas_param_request, var_url_id):
. var_get_titulo_tarea = get_object_or_404(tabla_tareas, id = var_url_id)
. () #paréntesis al final 'ejecuta la clase/modelo/tabla' pero no lo necesitaba en este caso

print(view_funcion_crear_tarea_param_request.GET['crear_tarea_col_titulo'])
print(view_funcion_crear_tarea_param_request.GET['crear_tarea_col_descripcion'])


"""

def view_funcion_tareas(view_funcion_tareas_param_request):
    queryset_tareas = tabla_tareas.objects.all()
    return render(view_funcion_tareas_param_request, 'tareas/tareas.html',{
        'ref_html_tareas': queryset_tareas
    })

def view_funcion_crear_proyecto(view_funcion_crear_proyecto_param_request):

    if view_funcion_crear_proyecto_param_request.method == 'GET':
        return render(view_funcion_crear_proyecto_param_request, 'proyectos/crear proyecto.html',{'ref_html_crear_proyecto': tabla_crear_proyecto})
    else:
        tabla_proyectos.objects.create(
        tab_proyectos_col_nombres = 
        view_funcion_crear_proyecto_param_request.POST['crear_proyecto_col_nombre'])
        return redirect('url name proyectos')


def view_funcion_crear_tarea(view_funcion_crear_tarea_param_request):

    if view_funcion_crear_tarea_param_request.method == 'GET':
        return render(view_funcion_crear_tarea_param_request, 'tareas/crear tarea.html',{'ref_html_crear_tarea': tabla_crear_tarea})
    else:
        tabla_tareas.objects.create(
        tab_tareas_col_nombre = 
        view_funcion_crear_tarea_param_request.POST['crear_tarea_col_nombre'],
        tab_tareas_col_descripcion = 
        view_funcion_crear_tarea_param_request.POST['crear_tarea_col_descripcion'],
        tab_tareas_col_proyecto_ref_id = 
        view_funcion_crear_tarea_param_request.POST['crear_tarea_col_proyecto'])
        return redirect('url name tareas')


"""
. cuando visita la página de esta forma no existe el título descripción
. si visitamos 'create task' sin parámetros me indica 'título no existe' entonces al momento de insertar da error 
. no debemos insertar datos con método GET este sirve para mostrar datos en la interfaz
. metodo POST para q servidor reciba datos (cuando el formulario va a enviar los datos)
. en archivo crear tarea en el formulario establecemos método post en ves de action
. en views establecemos si request.método == GET (sirve para mostrar) voy a renderizar la interfaz
. caso contrario si visita otra vez otro método (ELSE/cualquier otro metodo) voy a procesar/guardar/insertan los datos a la base de datos 
. cuando termine de guarda voy a cambiar de página
. por el momento en vez de usar el metodo GET lo cambia a POST por que así lo establecimos en el formulario

"""

def view_funcion_detalle_proyecto(view_funcion_detalle_proyecto_param_request, detalle_proyecto):
    detalle_proyecto = get_object_or_404(tabla_proyectos,id=detalle_proyecto)
    # en filter no se puede usar id, puede que sea solo una propiedad especial, y nombre_id si es el nombre de una columna y tiene otro acceso o propiedad
    detalle_proyecto_tareas = tabla_tareas.objects.filter(tab_tareas_col_proyecto_ref_id=detalle_proyecto)
    #detalle_proyecto = tabla_proyectos.objects.get(id=detalle_proyecto)
    return render(view_funcion_detalle_proyecto_param_request, 'proyectos/detalle proyecto.html',{'ref_html_detalle_proyecto':detalle_proyecto,
                    'ref_html_detalle_proyecto_tareas':detalle_proyecto_tareas})
