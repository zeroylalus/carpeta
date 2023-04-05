""" ---> NOTA:
. este archivo fue creado por nosotros, por que cada app puede guardar sus propias urls/rutas, y django no lo hace automáticamente.
. donde se encuentren las rutas/urls deben de importarse las views para ejecuten el código de las funciones convencionales
. como se han separado en este archivo estas urls de esta app, se necesitan integrar al archivo urls original con include()
"""

# tambien podría ser 'from . import views' el punto significa ruta actual
from django.urls import path
from .views import view_funcion_hello
from .views import view_funcion_acerca_de
from .views import view_funcion_index

#función view_fun_hello puede extraer la variable var_params (especificar en típo de dato) en la ruta
urlpatterns = [
    path('',view_funcion_index),
    path('ruta_acerca_de/', view_funcion_acerca_de),
    path('hello/<str:var_params_ruta>',view_funcion_hello),
]