# Generated by Django 3.1.1 on 2020-12-14 11:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_etebase', '0035_auto_20201214_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='uid',
            field=models.CharField(db_index=True, max_length=43, unique=True, validators=[django.core.validators.RegexValidator(message='Not a valid UID', regex='^[a-zA-Z0-9\\-_]{20,}$')]),
        ),
    ]
