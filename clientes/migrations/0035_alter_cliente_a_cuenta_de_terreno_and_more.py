# Generated by Django 4.0.6 on 2022-08-30 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0034_alter_cliente_codigo_alter_cliente_colonia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='a_cuenta_de_terreno',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='abono_pago',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cantidad_en_conciliacion',
            field=models.IntegerField(default=0, help_text='Cantidad en Conciliacion'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='codigo',
            field=models.CharField(default='30082022122755ACI', max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='colonia',
            field=models.CharField(choices=[('RLgK8fhYLlLwHQ', 'RLgK8fhYLlLwHQ'), ('gkQ88ZqP0OJlFLE', 'gkQ88ZqP0OJlFLE'), ('fZMLva4hxpr5kOF', 'fZMLva4hxpr5kOF'), ('eZFIrXs2sT', 'eZFIrXs2sT'), ('QR1sZwWZsXQGF', 'QR1sZwWZsXQGF'), ('6BPaOfmYHl', '6BPaOfmYHl'), ('uDS70N4S4HppSn', 'uDS70N4S4HppSn'), ('FQrlYmH8', 'FQrlYmH8'), ('jeDDusREDYAAr', 'jeDDusREDYAAr')], max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='compromiso_de_pago',
            field=models.IntegerField(default=0, help_text='Compromiso Pago'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='costo_del_terreno',
            field=models.IntegerField(default=0, help_text='Costo Terreno'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cp',
            field=models.CharField(choices=[('iPefq', 'iPefq'), ('KSzSG', 'KSzSG'), ('9BbYD', '9BbYD'), ('gZsW3', 'gZsW3')], max_length=350),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='deuda_de_terreno',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='forma_de_pago',
            field=models.CharField(choices=[('efectivo', 'Efectivo')], default='efectivo', max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='manzana',
            field=models.IntegerField(default=0, help_text='Ingresa la manzana'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='municipio',
            field=models.CharField(choices=[('Acajete', 'Acajete'), ('Acateno', 'Acateno'), ('Acatlán', 'Acatlán'), ('Acatzingo', 'Acatzingo'), ('Acteopan', 'Acteopan'), ('Ahuacatlán', 'Ahuacatlán'), ('Ahuatlán', 'Ahuatlán'), ('Ahuazotepec', 'Ahuazotepec'), ('Ahuehuetitla', 'Ahuehuetitla'), ('Ajalpan', 'Ajalpan'), ('Albino Zertuche', 'Albino Zertuche'), ('Aljojuca', 'Aljojuca'), ('Altepexi', 'Altepexi'), ('Amixtlán', 'Amixtlán'), ('Amozoc', 'Amozoc'), ('Aquixtla', 'Aquixtla'), ('Atempan', 'Atempan'), ('Atexcal', 'Atexcal'), ('Atlequizayan', 'Atlequizayan'), ('Atlixco', 'Atlixco'), ('Atoyatempan', 'Atoyatempan'), ('Atzala', 'Atzala'), ('Atzitzihuacán', 'Atzitzihuacán'), ('Atzitzintla', 'Atzitzintla'), ('Axutla', 'Axutla'), ('Ayotoxco de Guerrero', 'Ayotoxco de Guerrero'), ('Calpan', 'Calpan'), ('Caltepec', 'Caltepec'), ('Camocuautla', 'Camocuautla'), ('Cañada Morelos', 'Cañada Morelos'), ('Caxhuacan', 'Caxhuacan'), ('Chalchicomula de Sesma', 'Chalchicomula de Sesma'), ('Chapulco', 'Chapulco'), ('Chiautla', 'Chiautla'), ('Chiautzingo', 'Chiautzingo'), ('Chichiquila', 'Chichiquila'), ('Chiconcuautla', 'Chiconcuautla'), ('Chietla', 'Chietla'), ('Chigmecatitlán', 'Chigmecatitlán'), ('Chignahuapan', 'Chignahuapan'), ('Chignautla', 'Chignautla'), ('Chila de la Sal', 'Chila de la Sal'), ('Chila', 'Chila'), ('Chilchotla', 'Chilchotla'), ('Chinantla', 'Chinantla'), ('Coatepec', 'Coatepec'), ('Coatzingo', 'Coatzingo'), ('Cohetzala', 'Cohetzala'), ('Cohuecan', 'Cohuecan'), ('Coronango', 'Coronango'), ('Coxcatlán', 'Coxcatlán'), ('Coyomeapan', 'Coyomeapan'), ('Coyotepec', 'Coyotepec'), ('Cuapiaxtla de Madero', 'Cuapiaxtla de Madero'), ('Cuautempan', 'Cuautempan'), ('Cuautinchán', 'Cuautinchán'), ('Cuautlancingo', 'Cuautlancingo'), ('Cuayuca de Andrade', 'Cuayuca de Andrade'), ('Cuetzalan del Progreso', 'Cuetzalan del Progreso'), ('Cuyoaco', 'Cuyoaco'), ('Domingo Arenas', 'Domingo Arenas'), ('Eloxochitlán', 'Eloxochitlán'), ('Epatlán', 'Epatlán'), ('Esperanza', 'Esperanza'), ('Francisco Z. Mena', 'Francisco Z. Mena'), ('General Felipe Ángeles', 'General Felipe Ángeles'), ('Guadalupe Victoria', 'Guadalupe Victoria'), ('Guadalupe', 'Guadalupe'), ('Hermenegildo Galeana', 'Hermenegildo Galeana'), ('Honey', 'Honey'), ('Huaquechula', 'Huaquechula'), ('Huatlatlauca', 'Huatlatlauca'), ('Huauchinango', 'Huauchinango'), ('Huehuetla', 'Huehuetla'), ('Huehuetlán el Chico', 'Huehuetlán el Chico'), ('Huehuetlán el Grande', 'Huehuetlán el Grande'), ('Huejotzingo', 'Huejotzingo'), ('Hueyapan', 'Hueyapan'), ('Hueytamalco', 'Hueytamalco'), ('Hueytlalpan', 'Hueytlalpan'), ('Huitzilan de Serdán', 'Huitzilan de Serdán'), ('Huitziltepec', 'Huitziltepec'), ('Ixcamilpa de Guerrero', 'Ixcamilpa de Guerrero'), ('Ixcaquixtla', 'Ixcaquixtla'), ('Ixtacamaxtitlán', 'Ixtacamaxtitlán'), ('Ixtepec', 'Ixtepec'), ('Izúcar de Matamoros', 'Izúcar de Matamoros'), ('Jalpan', 'Jalpan'), ('Jolalpan', 'Jolalpan'), ('Jonotla', 'Jonotla'), ('Jopala', 'Jopala'), ('Juan C. Bonilla', 'Juan C. Bonilla'), ('Juan Galindo', 'Juan Galindo'), ('Juan N. Méndez', 'Juan N. Méndez'), ('La Magdalena Tlatlauquitepec', 'La Magdalena Tlatlauquitepec'), ('Lafragua', 'Lafragua'), ('Libres', 'Libres'), ('Los Reyes de Juárez', 'Los Reyes de Juárez'), ('Mazapiltepec de Juárez', 'Mazapiltepec de Juárez'), ('Mixtla', 'Mixtla'), ('Molcaxac', 'Molcaxac'), ('Naupan', 'Naupan'), ('Nauzontla', 'Nauzontla'), ('Nealtican', 'Nealtican'), ('Nicolás Bravo', 'Nicolás Bravo'), ('Nopalucan', 'Nopalucan'), ('Ocotepec', 'Ocotepec'), ('Ocoyucan', 'Ocoyucan'), ('Olintla', 'Olintla'), ('Oriental', 'Oriental'), ('Pahuatlán', 'Pahuatlán'), ('Palmar de Bravo', 'Palmar de Bravo'), ('Pantepec', 'Pantepec'), ('Petlalcingo', 'Petlalcingo'), ('Piaxtla', 'Piaxtla'), ('Puebla', 'Puebla'), ('Quecholac', 'Quecholac'), ('Quimixtlán', 'Quimixtlán'), ('Rafael Lara Grajales', 'Rafael Lara Grajales'), ('San Andrés Cholula', 'San Andrés Cholula'), ('San Antonio Cañada', 'San Antonio Cañada'), ('San Diego la Mesa Tochimiltzingo', 'San Diego la Mesa Tochimiltzingo'), ('San Felipe Teotlalcingo', 'San Felipe Teotlalcingo'), ('San Felipe Tepatlán', 'San Felipe Tepatlán'), ('San Gabriel Chilac', 'San Gabriel Chilac'), ('San Gregorio Atzompa', 'San Gregorio Atzompa'), ('San Jerónimo Tecuanipan', 'San Jerónimo Tecuanipan'), ('San Jerónimo Xayacatlán', 'San Jerónimo Xayacatlán'), ('San José Chiapa', 'San José Chiapa'), ('San José Miahuatlán', 'San José Miahuatlán'), ('San Juan Atenco', 'San Juan Atenco'), ('San Juan Atzompa', 'San Juan Atzompa'), ('San Martín Texmelucan', 'San Martín Texmelucan'), ('San Martín Totoltepec', 'San Martín Totoltepec'), ('San Matías Tlalancaleca', 'San Matías Tlalancaleca'), ('San Miguel Ixitlán', 'San Miguel Ixitlán'), ('San Miguel Xoxtla', 'San Miguel Xoxtla'), ('San Nicolás Buenos Aires', 'San Nicolás Buenos Aires'), ('San Nicolás de los Ranchos', 'San Nicolás de los Ranchos'), ('San Pablo Anicano', 'San Pablo Anicano'), ('San Pedro Cholula', 'San Pedro Cholula'), ('San Pedro Yeloixtlahuaca', 'San Pedro Yeloixtlahuaca'), ('San Salvador el Seco', 'San Salvador el Seco'), ('San Salvador el Verde', 'San Salvador el Verde'), ('San Salvador Huixcolotla', 'San Salvador Huixcolotla'), ('San Sebastián Tlacotepec', 'San Sebastián Tlacotepec'), ('Santa Catarina Tlaltempan', 'Santa Catarina Tlaltempan'), ('Santa Inés Ahuatempan', 'Santa Inés Ahuatempan'), ('Santa Isabel Cholula', 'Santa Isabel Cholula'), ('Santiago Miahuatlán', 'Santiago Miahuatlán'), ('Santo Tomás Hueyotlipan', 'Santo Tomás Hueyotlipan'), ('Soltepec', 'Soltepec'), ('Tecali de Herrera', 'Tecali de Herrera'), ('Tecamachalco', 'Tecamachalco'), ('Tecomatlán', 'Tecomatlán'), ('Tehuacán', 'Tehuacán'), ('Tehuitzingo', 'Tehuitzingo'), ('Tenampulco', 'Tenampulco'), ('Teopantlán', 'Teopantlán'), ('Teotlalco', 'Teotlalco'), ('Tepanco de López', 'Tepanco de López'), ('Tepango de Rodríguez', 'Tepango de Rodríguez'), ('Tepatlaxco de Hidalgo', 'Tepatlaxco de Hidalgo'), ('Tepeaca', 'Tepeaca'), ('Tepemaxalco', 'Tepemaxalco'), ('Tepeojuma', 'Tepeojuma'), ('Tepetzintla', 'Tepetzintla'), ('Tepexco', 'Tepexco'), ('Tepexi de Rodríguez', 'Tepexi de Rodríguez'), ('Tepeyahualco de Cuauhtémoc', 'Tepeyahualco de Cuauhtémoc'), ('Tepeyahualco', 'Tepeyahualco'), ('Tetela de Ocampo', 'Tetela de Ocampo'), ('Teteles de Ávila Castillo', 'Teteles de Ávila Castillo'), ('Teziutlán', 'Teziutlán'), ('Tianguismanalco', 'Tianguismanalco'), ('Tilapa', 'Tilapa'), ('Tlachichuca', 'Tlachichuca'), ('Tlacotepec de Benito Juárez', 'Tlacotepec de Benito Juárez'), ('Tlacuilotepec', 'Tlacuilotepec'), ('Tlahuapan', 'Tlahuapan'), ('Tlaltenango', 'Tlaltenango'), ('Tlanepantla', 'Tlanepantla'), ('Tlaola', 'Tlaola'), ('Tlapacoya', 'Tlapacoya'), ('Tlapanalá', 'Tlapanalá'), ('Tlatlauquitepec', 'Tlatlauquitepec'), ('Tlaxco', 'Tlaxco'), ('Tochimilco', 'Tochimilco'), ('Tochtepec', 'Tochtepec'), ('Totoltepec de Guerrero', 'Totoltepec de Guerrero'), ('Tulcingo', 'Tulcingo'), ('Tuzamapan de Galeana', 'Tuzamapan de Galeana'), ('Tzicatlacoyan', 'Tzicatlacoyan'), ('Venustiano Carranza', 'Venustiano Carranza'), ('Vicente Guerrero', 'Vicente Guerrero'), ('Xayacatlán de Bravo', 'Xayacatlán de Bravo'), ('Xicotepec', 'Xicotepec'), ('Xicotlán', 'Xicotlán'), ('Xiutetelco', 'Xiutetelco'), ('Xochiapulco', 'Xochiapulco'), ('Xochiltepec', 'Xochiltepec'), ('Xochitlán de Vicente Suárez', 'Xochitlán de Vicente Suárez'), ('Xochitlán Todos Santos', 'Xochitlán Todos Santos'), ('Yaonáhuac', 'Yaonáhuac'), ('Yehualtepec', 'Yehualtepec'), ('Zacapala', 'Zacapala'), ('Zacapoaxtla', 'Zacapoaxtla'), ('Zacatlán', 'Zacatlán'), ('Zapotitlán de Méndez', 'Zapotitlán de Méndez'), ('Zapotitlán', 'Zapotitlán'), ('Zaragoza', 'Zaragoza'), ('Zautla', 'Zautla'), ('Zihuateutla', 'Zihuateutla'), ('Zinacatepec', 'Zinacatepec'), ('Zongozotla', 'Zongozotla'), ('Zoquiapan', 'Zoquiapan'), ('Zoquitlán', 'Zoquitlán')], default='Puebla', max_length=350),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='notificaciones',
            field=models.CharField(choices=[('recibo', 'Recibo')], default='recibo', max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numero_lote',
            field=models.IntegerField(default=0, help_text='Ingresa numero de lote'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='comprobante_de_pago',
            field=models.FileField(null=True, upload_to='clientes/static/images/'),
        ),
    ]
