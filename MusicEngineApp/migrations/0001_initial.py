# Generated by Django 4.1.7 on 2023-04-08 10:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(max_length=100)),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('material',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicEngineApp.material')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicEngineApp.sala')),
                (
                'tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicEngineApp.tecnico')),
            ],
        ),
        migrations.CreateModel(
            name='HorarioTecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                (
                'tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicEngineApp.tecnico')),
            ],
        ),
    ]
