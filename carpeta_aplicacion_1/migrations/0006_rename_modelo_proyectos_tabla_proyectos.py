# Generated by Django 4.1.7 on 2023-04-06 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpeta_aplicacion_1', '0005_rename_clase_proyectos_modelo_proyectos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='modelo_proyectos',
            new_name='tabla_proyectos',
        ),
    ]
