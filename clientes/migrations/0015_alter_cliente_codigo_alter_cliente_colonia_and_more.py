# Generated by Django 4.0.6 on 2022-08-15 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0014_alter_cliente_codigo_alter_cliente_colonia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='codigo',
            field=models.CharField(default='14082022190557ACI', max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='colonia',
            field=models.CharField(choices=[('gWz1CqBmikL', 'gWz1CqBmikL'), ('rugYLSBVEw68', 'rugYLSBVEw68'), ('2x8QQ7pmDdOEuP', '2x8QQ7pmDdOEuP'), ('6yTaNVa7', '6yTaNVa7'), ('cT5EYQp', 'cT5EYQp'), ('lCltfcT', 'lCltfcT'), ('Fe84Yyo1banACG', 'Fe84Yyo1banACG'), ('rZERLE024lhCo1x', 'rZERLE024lhCo1x'), ('ZkIrweozizIw6i', 'ZkIrweozizIw6i')], default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cp',
            field=models.CharField(choices=[('SgKf4', 'SgKf4'), ('xiOgP', 'xiOgP'), ('wf79q', 'wf79q'), ('cF17g', 'cF17g'), ('r68Hr', 'r68Hr'), ('Tx6ZV', 'Tx6ZV'), ('ITPa6', 'ITPa6'), ('EdcU9', 'EdcU9'), ('FfsbB', 'FfsbB'), ('S1wh7', 'S1wh7')], default=1, max_length=150),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='municipio',
            field=models.CharField(choices=[('iYH02ba5oWH5a7u', 'iYH02ba5oWH5a7u'), ('uyjOvniFFw7N', 'uyjOvniFFw7N'), ('rGR5ptv', 'rGR5ptv'), ('L2qJhR1o8', 'L2qJhR1o8')], default=1, max_length=150),
        ),
    ]
