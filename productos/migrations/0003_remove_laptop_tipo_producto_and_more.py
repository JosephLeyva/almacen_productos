# Generated by Django 4.0.5 on 2022-07-04 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_laptop_zapato'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='tipo_producto',
        ),
        migrations.RemoveField(
            model_name='zapato',
            name='tipo_producto',
        ),
    ]
