"""
permite que una clase se extienda con nuevas características para que luego se vuelva un formulario de html
crear_tarea_col_titulo: no es para la base de datos, es para enviarselo al html y lo transforma en un input de tipo texto
forms da una propiedad para heredar su clase llamada Form
widget: si queremos que sea text area, heredado desde forms.textarea
"""

from django import forms

class tabla_crear_tarea(forms.Form):
    crear_tarea_col_nombre = forms.CharField(label='label (Título de la tarea)', max_length=200)
    crear_tarea_col_descripcion = forms.CharField(label='label (Descripción de la tarea)',widget=forms.Textarea)
    crear_tarea_col_proyecto = forms.IntegerField(label='label (# Proyecto de la tarea)')

class tabla_crear_proyecto(forms.Form):
    crear_proyecto_col_nombre = forms.CharField(label='label (Título del proyecto)', max_length=200)
