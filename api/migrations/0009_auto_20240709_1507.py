# Generated by Django 2.2.4 on 2024-07-09 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20240703_1551'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'verbose_name': 'comentario', 'verbose_name_plural': 'comentarios'},
        ),
        migrations.AlterModelOptions(
            name='direccion',
            options={'verbose_name': 'dirección', 'verbose_name_plural': 'direcciones'},
        ),
        migrations.AlterModelOptions(
            name='etiqueta',
            options={'verbose_name': 'etiqueta', 'verbose_name_plural': 'etiquetas'},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'ticket', 'verbose_name_plural': 'tickets'},
        ),
        migrations.AddField(
            model_name='comentario',
            name='titulo',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comentario',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
