# Generated by Django 4.1 on 2022-10-15 18:07

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_reserva'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='RES_VALOR_RESERVA',
        ),
        migrations.AddField(
            model_name='departamento',
            name='DEP_CHECK_LIST',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='departamento',
            name='DEP_CHECK_LIST_FECHA',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='departamento',
            name='DEP_INVENTARIO',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inventario',
            name='INV_HERVIDOR',
            field=models.BooleanField(default=False, verbose_name='Hervidor'),
        ),
        migrations.AddField(
            model_name='inventario',
            name='INV_HERVIDOR_VALOR',
            field=models.IntegerField(default=25000),
        ),
        migrations.AddField(
            model_name='inventario',
            name='INV_HORNOELECTRICO_VALOR',
            field=models.IntegerField(default=25000),
        ),
        migrations.AddField(
            model_name='inventario',
            name='INV_MICROONDAS_VALOR',
            field=models.IntegerField(default=25000),
        ),
        migrations.AddField(
            model_name='inventario',
            name='INV_PARRILLA',
            field=models.BooleanField(default=False, verbose_name='Parrilla'),
        ),
        migrations.AddField(
            model_name='inventario',
            name='INV_PARRILLA_VALOR',
            field=models.IntegerField(default=25000),
        ),
        migrations.AddField(
            model_name='inventario',
            name='INV_REFRIGERADOR',
            field=models.BooleanField(default=False, verbose_name='Refrigerador'),
        ),
        migrations.AddField(
            model_name='inventario',
            name='INV_REFRIGERADOR_VALOR',
            field=models.IntegerField(default=25000),
        ),
        migrations.AddField(
            model_name='inventario',
            name='INV_TELEVISOR',
            field=models.BooleanField(default=False, verbose_name='Televisor'),
        ),
        migrations.AddField(
            model_name='inventario',
            name='INV_TELEVISOR_VALOR',
            field=models.IntegerField(default=25000),
        ),
        migrations.AddField(
            model_name='reserva',
            name='RES_CHECK_IN',
            field=models.BooleanField(default=False, verbose_name='Check In'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='RES_CHECK_OUT',
            field=models.BooleanField(default=False, verbose_name='Check Out'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='RES_CLIST_IN',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='RES_CLIST_OUT',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='RES_DESEA_TOUR_1',
            field=models.BooleanField(default=False, verbose_name='Desea tour 1'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='RES_DESEA_TOUR_2',
            field=models.BooleanField(default=False, verbose_name='Desea tour 2'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='RES_DESEA_TOUR_3',
            field=models.BooleanField(default=False, verbose_name='Desea tour 3'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='RES_TRANSPORTE',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.transporte'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva',
            name='RES_VALIDA_CLIENTE',
            field=models.BooleanField(default=False, verbose_name='Cliente válido'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='RES_VALOR_DEPARTAMENTO',
            field=models.IntegerField(blank=True, null=True, verbose_name='Valor del departamento'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='RES_VALOR_FINAL_RESERVA',
            field=models.IntegerField(default=1, verbose_name='Valor final de reserva'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva',
            name='RES_VALOR_MULTAS',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Valor multas'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='RES_VALOR_SERVICIOS_EXTRA',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Valor de servicios extra'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='RES_VALOR_TOTAL',
            field=models.IntegerField(blank=True, null=True, verbose_name='Valor total de la reserva'),
        ),
    ]
