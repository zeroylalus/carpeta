""" ---> NOTA:
. este archivo fue creado por nosotros, por que cada app puede guardar sus propias urls/rutas, y django no lo hace automáticamente.
. donde se encuentren las rutas/urls deben de importarse las views para ejecuten el código de las funciones convencionales
. como se han separado en este archivo estas urls de esta app, se necesitan integrar al archivo urls original con include()
"""

# tambien podría ser 'from . import views' el punto significa ruta actual
from django.urls import path

from .views import view_funcion_hello_int
from .views import view_funcion_hello_str

from .views import view_funcion_acerca_de
from .views import view_funcion_index

from .views import view_funcion_proyectos
from .views import view_funcion_tareas

#función view_fun_hello puede extraer la variable var_params (especificar en típo de dato) en la ruta
urlpatterns = [

    # rutas de ejemplo:

    path('string/<str:var_params_ruta>',view_funcion_hello_str),
    path('entero/<int:var_params_ruta_int>',view_funcion_hello_int),

    # rutas de datos:

    path('',view_funcion_index),
    path('ruta_acerca_de/', view_funcion_acerca_de),

    # rutas que van a recibir y enviar información:

    path('proyectos/',view_funcion_proyectos),
    path('tareas/<int:var_url_id>',view_funcion_tareas),
]