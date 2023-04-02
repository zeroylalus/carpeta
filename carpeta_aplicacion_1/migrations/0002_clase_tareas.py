# archivo creado al hacer migraciones de datos de modelos de la app a la base de datos
# Generated by Django 4.1.7 on 2023-04-02 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carpeta_aplicacion_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='clase_tareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_clase_tareas', models.CharField(max_length=200)),
                ('descripcion_clase_tareas', models.TextField()),
                ('n_proyecto_clase_tareas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carpeta_aplicacion_1.clase_proyectos')),
            ],
        ),
    ]