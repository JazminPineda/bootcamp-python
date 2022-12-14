# Generated by Django 4.1.2 on 2022-10-09 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('data_of_birth', models.DateField(blank=True, null=True)),
                ('data_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Por el nombre del genero ', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('summary', models.TextField(help_text='Resumen libro ', max_length=100)),
                ('año', models.CharField(help_text='Año de producción', max_length=4)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogos_peli.author')),
                ('genero', models.ManyToManyField(to='catalogos_peli.genero')),
            ],
        ),
        migrations.CreateModel(
            name='PeliculaInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inprint', models.CharField(max_length=200)),
                ('alquilado', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('o', 'Prestado'), ('a', 'Disponible'), ('r', 'Reservado')], default='m', help_text='Disponibilidad del libro', max_length=1)),
                ('video', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogos_peli.pelicula')),
            ],
        ),
    ]
