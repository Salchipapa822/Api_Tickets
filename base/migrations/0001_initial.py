# Generated by Django 5.0.7 on 2024-07-15 17:28

import base.models
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, validators=[base.models.validate_only_letters])),
            ],
            options={
                'verbose_name': 'dirección',
                'verbose_name_plural': 'direcciones',
            },
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, validators=[base.models.validate_only_letters])),
            ],
            options={
                'verbose_name': 'etiqueta',
                'verbose_name_plural': 'etiquetas',
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('cedula', models.IntegerField(primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MinValueValidator(1000000, message='La cédula debe tener al menos 8 dígitos.'), django.core.validators.MaxValueValidator(999999999, message='La cédula debe tener como máximo 9 dígitos.')])),
                ('nombre', models.CharField(max_length=100, validators=[base.models.validate_only_letters])),
                ('apellido', models.CharField(max_length=100, validators=[base.models.validate_only_letters])),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_cierre', models.DateTimeField(null=True)),
                ('etiqueta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.etiqueta')),
                ('presentado_en', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.direccion')),
                ('presentado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.personal')),
                ('resuelto_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ticket',
                'verbose_name_plural': 'tickets',
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='autor')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='base.ticket')),
            ],
            options={
                'verbose_name': 'comentario',
                'verbose_name_plural': 'comentarios',
            },
        ),
    ]
