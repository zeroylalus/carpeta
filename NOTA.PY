"""
VSCODE:
F1 : lista de opciones en vscode
'select interpreter' : establecer la terminal con el entorno virtual

-------------------------------

TERMINAL:
'cls' : limpiar consola

-------------------------------

VIRTUALENV:
'pip install virtualenv'
'virtualenv 'nombre_entorno_virtual'' : CREAR ENTORNO (ESTO CREA UNA CARPETA)
".\entorno_virtual\Scripts\activate" : 'ACTIVAR ENTORNO

-------------------------------

DJANGO:
'django-admin startproject nombre_proyecto_django .' : CREAR PROYECTO DJANGO ( ' .' AL FINAL HACE QUE NO CREE DOBLE CARPETA)
'__pycache__' : la carpeta guarda código que ya compilo python para que se ejecute mas rápido

-------------------------------
PARAMS:
recibir datos desde navegador para pasarlo por operaciones de una base de datos
 

-------------------------------

SERVIDOR:
ORM? en cada cambio, vuelve a ejecutar todo el proyecto automaticamente

BASE DE DATOS:
1. 'python manage.py makemigrations nombre_carpeta_app' inicialmente no sirve por que python ya tiene 'migraciones' hechas de database por defecto de ORM
1.1 pero el comando migra los datos de los modelos de las apps en general o la especificada y crea archivos migrations dentro de carpeta migrations de app
2. 'python manage.py migrate nombre_carpeta_app' ejecuta las 'migraciones' crea las tablas dentro de nuestra base de datos de apps en general o la especificada
2.1 el 'script' del archivo db.sqlite3 es el que ejecuta las migraciones, este proceso funciona en cualquier base de datos (sql: mysql, postgres, oracle, etc.) con la configuración correcta, para eso se crea un modelo en la carpeta de la app
2.2. para crear tablas (productos, categorías, etc.) es necesario crear un 'modelo' (código python que se va a transformar en una tabla SQL), dentro del archivo 'models.py', se crea una clase, que hera los modelos que da django, y de allí llama a la clase model, que permiten especificar las tablas

-------------------------------

MINI CLASE SHELL? para interactuar con database
- 'python manage.py shell' iniciar la consola
- 'from app.models import proyectos, tareas': importar tablas desde archivo models de app
- 'proyectos(nombre = 'proyecto 1').save()': ingresa dato en fila en turno en columna nombre
- 'proyectos.objects.all()': obtiene set query de ids
- 'proyectos.objects.all().delete()': elimina todos los datos de proyectos
- 'proyectos.objects.get(id=1)': obtiene query con id, donde id=1
- 'proyectos.objects.get(id=1).delete()': elimina la fila donde id=1
- 'proyectos.objects.get(id=7).tareas_set.create(titulo = 'tarea 1')': crea dato en fila en turno en columna titulo de tabla tareas con referencia de la tabla proyectos con id 7.
- 'proyectos.objects.get(id=7).tareas_set.all()': obtiene set query de ids de tareas relacionados a proyectos con id 7
- 'proyectos.objects.get(id=7).tareas_set.all().delete()': elimina todos los datos de tareas relacionados a proyectos con id 7
- 'proyectos.objects.get(id=7).tareas_set.get(id=1)': obtiene dato donde id=1 de tareas relacionados a proyectos con id 7
- 'proyectos.objects.get(id=7).tareas_set.get(id=1).delete()': elimina dato donde id=1 de tareas relacionados a proyectos con id 7

-------------------------------

CARPETAS:

PROYECTO GLOBAL Y APLICACIONES
'python manage.py startapp carpeta_aplicacion_1' : crea carpeta de applicacion interna del proyecto global
    carpeta_proyecto_django : administra 'proyecto global'
    carpeta_aplicacion_1 : administra una parte del 'proyecto global'

MIGRATIONS:
SE MODIFICA AUTOMATICAMENTE al llenar datos en la base de datos
django no requiere consultas SQL x modulo ORM base de datos interactua atraves de código de python

-------------------------------

ORGANIGRAMA: 
¿como se le llama a esta modalidad o proceso para crear y si existen?

. creamos un proyecto con 'django-admin startproject proyecto'
. creamos una app con 'python manage.py startapp app'
. agregamos nuestra app a la lista de apps del archivo settings dentro de proyecto
. dentro de app en archivo views creamos función para enviar contenido al navegador
. dentro de app creamos archivo que aloja rutas que ejecutan funciones importadas de views
. incluimos urls dentro de app, al archivo 'urls' dentro de proyecto con módulo include.
. Creamos modelo dentro de app, en archivo models con clase: proyectos, tipo de dato: texto
. Creamos modelo dentro de app, en archivo models con clase: tareas, 1er tipo de dato: texto, 2do tipo de dato: texto, 3er tipo de dato: foreignkey que tiene relacion con proyectos

-------------------------------

para despues:
. Creamos modelo dentro de app, ventas(#venta, cliente, producto, cantidad_venta, precio_venta)
. Creamos modelo dentro de app, productos(producto, sku, cantidad, precio)
. Creamos modelo dentro de app, clientes(nombre, telefono, direccion)
. migramos datos de modelos dentro de app a la base de datos

"""