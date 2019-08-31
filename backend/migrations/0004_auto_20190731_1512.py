# Generated by Django 2.2.3 on 2019-07-31 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20190731_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Date Creation Client'),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_delivery_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date de premiere livraison'),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_delivery_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date de dernière livraison'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='date_creation',
            field=models.DateField(auto_now_add=True, verbose_name='Date Creation Livraison'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='date_livraison',
            field=models.DateField(blank=True, null=True, verbose_name='Date Livraison'),
        ),
        migrations.AlterField(
            model_name='parcel',
            name='date_creation',
            field=models.DateField(auto_now_add=True, verbose_name='Date création colis'),
        ),
        migrations.AlterField(
            model_name='parcel',
            name='date_delivery',
            field=models.DateField(blank=True, null=True, verbose_name='Date livraison colis'),
        ),
    ]
