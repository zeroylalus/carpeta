# este archivo fue creado por nosotros, por que cada app puede guardar sus propias urls/rutas, y django no lo hace automáticamente.

# donde se encuentren las rutas/urls deben de importarse las views para ejecuten el código de las funciones convencionales
# como se han separado en este archivo estas urls de esta app, se necesitan integrar al archivo urls original con include()

from django.urls import path
# tambien podría ser 'from . import views' el punto significa ruta actual
from .views import view_fun_hello
from .views import view_fun_acerca_de

urlpatterns = [
    path('', view_fun_hello),
    path('ruta_acerca_de/', view_fun_acerca_de),
]

"""
path('',views.index, name='index'),
path('about/',views.about, name='about'),
path('hello/<str:username>',views.hello, name='hello'),
path('projects/',views.projects, name='projects'),
path('projects/<int:id>',views.project_detail, name='project_detail'),
path('tasks/',views.tasks, name='tasks'),
path('create_task/',views.create_task, name='create_task'),
path('create_project/',views.create_project, name='create_project')"""