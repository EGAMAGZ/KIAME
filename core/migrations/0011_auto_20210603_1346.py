# Generated by Django 3.1.2 on 2021-06-03 18:46

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_marketrate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketrate',
            name='document',
            field=models.FileField(upload_to='market_rate/', validators=[core.validators.validate_file_extension], verbose_name='Documento'),
        ),
    ]