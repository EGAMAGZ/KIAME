# Generated by Django 3.1.2 on 2021-06-18 16:04

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20210615_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, upload_to='description/', validators=[core.validators.validate_file_extension], verbose_name='Documento')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
            ],
            options={
                'verbose_name': 'Descripción de Proyecto',
                'verbose_name_plural': 'Descripcion de Proyecto',
            },
        ),
    ]
