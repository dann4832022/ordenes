# Generated by Django 4.0 on 2024-02-18 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carga_archivos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivoexcel',
            name='fecha',
            field=models.DateField(null=True),
        ),
    ]
