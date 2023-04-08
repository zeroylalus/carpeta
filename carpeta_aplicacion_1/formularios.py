"""
permite que una clase se extienda con nuevas características para que luego se vuelva un formulario de html
crear_tarea_col_titulo: no es para la base de datos, es para enviarselo al html y lo transforma en un input de tipo texto
forms da una propiedad para heredar su clase llamada Form
widget=forms.Textarea: si queremos que sea text area, heredado desde forms.textarea
widget=forms.TextInput(attrs={class:''}): para agregar estilos a formulario
"""

from django import forms

class tabla_crear_tarea(forms.Form):
    crear_tarea_col_nombre = forms.CharField(label='label (Título de la tarea)', max_length=200, widget=forms.TextInput(attrs={'class':'formulario'}))
    crear_tarea_col_descripcion = forms.CharField(label='label (Descripción de la tarea)',widget=forms.Textarea(attrs={'class':'formulario'}))
    crear_tarea_col_proyecto = forms.IntegerField(label='label (# Proyecto de la tarea)',widget=forms.TextInput(attrs={'class':'formulario'}))

class tabla_crear_proyecto(forms.Form):
    crear_proyecto_col_nombre = forms.CharField(label='label (Título del proyecto)', max_length=200, widget=forms.TextInput(attrs={'class': 'formulario'}))
