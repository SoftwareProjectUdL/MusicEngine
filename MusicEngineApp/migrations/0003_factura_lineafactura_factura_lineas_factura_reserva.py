# Generated by Django 4.1.7 on 2023-04-25 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MusicEngineApp', '0002_material_cantidad_material_estado_alter_reserva_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LineaFactura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('concepto', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicEngineApp.factura')),
            ],
        ),
        migrations.AddField(
            model_name='factura',
            name='lineas',
            field=models.ManyToManyField(related_name='lineas', to='MusicEngineApp.lineafactura'),
        ),
        migrations.AddField(
            model_name='factura',
            name='reserva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicEngineApp.reserva'),
        ),
    ]