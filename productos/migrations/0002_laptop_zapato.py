# Generated by Django 4.0.5 on 2022-07-04 03:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('sku', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
                ('marca', models.CharField(max_length=30)),
                ('costo', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('tipo_producto', models.CharField(choices=[('TELEVISOR', 'Televisor'), ('LAPTOP', 'Laptop'), ('ZAPATO', 'Zapato')], default='TELEVISOR', max_length=20)),
                ('procesador', models.CharField(max_length=20)),
                ('memoria_ram', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Zapato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('sku', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
                ('marca', models.CharField(max_length=30)),
                ('costo', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('tipo_producto', models.CharField(choices=[('TELEVISOR', 'Televisor'), ('LAPTOP', 'Laptop'), ('ZAPATO', 'Zapato')], default='TELEVISOR', max_length=20)),
                ('material', models.CharField(max_length=20)),
                ('numero', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
