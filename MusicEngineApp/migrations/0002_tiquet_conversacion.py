# Generated by Django 4.1.7 on 2023-05-23 22:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('MusicEngineApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiquet',
            name='conversacion',
            field=models.ManyToManyField(related_name='conversacion', to='MusicEngineApp.conversaciontiquet'),
        ),
    ]
