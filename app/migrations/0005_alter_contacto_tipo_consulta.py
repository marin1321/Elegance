# Generated by Django 3.2.1 on 2021-06-16 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210607_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='tipo_consulta',
            field=models.CharField(choices=[['Consulta', 'Consulta'], ['Reclamo', 'Reclamo'], ['Sugerencia', 'Sugerencia'], ['Felitaciones', 'Felitaciones']], max_length=14),
        ),
    ]