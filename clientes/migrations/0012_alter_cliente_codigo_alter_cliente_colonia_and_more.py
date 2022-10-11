# Generated by Django 4.0.6 on 2022-08-15 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0011_alter_cliente_codigo_alter_cliente_colonia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='codigo',
            field=models.CharField(default='14082022190307ACI', max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='colonia',
            field=models.CharField(choices=[('yvsPPwKG8Ifle', 'yvsPPwKG8Ifle'), ('kWdxw7coqtP6', 'kWdxw7coqtP6'), ('rrZsQeCuz65f6', 'rrZsQeCuz65f6'), ('Emwj31ER', 'Emwj31ER'), ('xKVwxbHHn', 'xKVwxbHHn'), ('Qc4YvVyBF9', 'Qc4YvVyBF9'), ('oc6u3', 'oc6u3')], default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cp',
            field=models.CharField(choices=[('WGLAp', 'WGLAp'), ('TlVdB', 'TlVdB'), ('DDEof', 'DDEof'), ('CKsbC', 'CKsbC'), ('MaTw1', 'MaTw1'), ('KBPom', 'KBPom'), ('lPzSU', 'lPzSU'), ('gsxNr', 'gsxNr'), ('hW6gl', 'hW6gl'), ('CfN5B', 'CfN5B')], default=1, max_length=150),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='municipio',
            field=models.CharField(choices=[('30WfBFlFKV', '30WfBFlFKV'), ('0X6mLUmR3KaY4', '0X6mLUmR3KaY4'), ('bNb3XkkXSgW', 'bNb3XkkXSgW'), ('FyE379', 'FyE379'), ('o7o5gAx9', 'o7o5gAx9'), ('gFQHh1g3Z', 'gFQHh1g3Z')], default=1, max_length=150),
        ),
    ]
