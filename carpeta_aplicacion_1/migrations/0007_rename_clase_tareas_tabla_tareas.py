# Generated by Django 4.1.7 on 2023-04-06 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpeta_aplicacion_1', '0006_rename_modelo_proyectos_tabla_proyectos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='clase_tareas',
            new_name='tabla_tareas',
        ),
    ]
