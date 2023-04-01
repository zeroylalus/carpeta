# NOTA ---> no esta tan relacionados con desarrollo si no en su ejecución, estando en producción "servimos" ese contenido, django no se ocupa de eso, configuracion para modulos 

# -------------  ARCHIVO ORIGINAL CREADO X DJANGO  ----------------------------

"""
WSGI config for carpeta_proyecto_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carpeta_proyecto_django.settings')

application = get_wsgi_application()
