# Generated by Django 4.1 on 2022-10-15 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_remove_reserva_res_valor_reserva_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='RES_VALOR_FINAL_RESERVA',
            field=models.IntegerField(blank=True, null=True, verbose_name='Valor final de reserva'),
        ),
    ]