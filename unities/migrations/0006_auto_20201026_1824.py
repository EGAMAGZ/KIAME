# Generated by Django 3.1.2 on 2020-10-27 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unities', '0005_auto_20201024_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unity',
            options={'ordering': ['number'], 'verbose_name': 'Unidad', 'verbose_name_plural': 'Unidades'},
        ),
    ]