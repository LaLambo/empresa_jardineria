# Generated by Django 4.2.7 on 2025-03-28 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('disponibilidad', models.CharField(max_length=200)),
                ('tipo_servicio', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Realizada', 'Realizada'), ('Cancelada', 'Cancelada')], default='Pendiente', max_length=50)),
                ('metros_cuadrados', models.FloatField()),
            ],
        ),
    ]
