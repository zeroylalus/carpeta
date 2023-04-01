""" ---> NOTA:
BASE_DIR: indica dónde están los directorios que contiene el proyecto
SECRET_KEY: mejorar la encriptación de los usuarios o generar datos a compartir entre el navegador y el servidor (dato aleatorio a modificar)
DEBUG: modo desarrollo = true /producción = false: para que no 'de tanta información' accede distintos lugares, usuarios
ALLOWED_HOSTS: permite al servidor web decirle qué direcciones tienen permitido consultar a nuestro servidor
INSTALLED_APPS:
    1. cuando creamos una carpeta creamos un 'proyecto'
    2. los 'proyectos' se dividen en distintas 'aplicaciones'
    3. django permite crear mas 'aplicaciones' dentro de este 'proyecto'
    4. para configurar esas 'aplicaciones' se añaden en 'INSTALLED_APPS'
    5. 'INSTALLED_APPS' ya trae aplicaciones 'instaladas' por defecto
MIDDLEWARE: para decirle a django si va a procesar 'determinado tipo de datos de alguna forma' se pueden agregar mas
TEMPLATES: sirve en modo de produccion requieren de otros modulos...
WSGI_APPLICATION: sirve en modo de produccion requieren de otros modulos...
ROOT_URLCONF: ¿establece la direccion de las urls? 
DATABASES:
    1. nos dice a qué base de datos estamos conectados
    2. por defecto está conectado a 'motor de base de datos' > biblioteca 'django.db.backends.sqlite3' > módulo de conexión 'sqlite3'
    3. 'NAME' direccion de la base de datos
    4. puedo especificar con otro 'string' en la biblioteca para conectar a otra base de datos (postgres, oracle, microsoft sql server, etc.) 
AUTH_PASSWORD_VALIDATORS: configuración relacionada a la válidación de contraseñas al momento de que se autentican los usuarios
LANGUAGE_CODE: lenguaje por defecto
TIME_ZONE: zona horario
USE_I18N: establecerlos distintos lenguajes
USE_TZ: establecerlos distintos lenguajes
STATIC_URL: para decir donde están los archivos estáticos (archivos CSS, HTML, JAVASCRIPT)
"""

# -------------  ARCHIVO ORIGINAL CREADO X DJANGO  ----------------------------


"""
Django settings for carpeta_proyecto_django project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kv2^p60m9wm#ct690=tg5!6dufcqq8fe*y-od-s4f^t@x&hdtx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'carpeta_proyecto_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'carpeta_proyecto_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
