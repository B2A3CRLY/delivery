# Generated by Django 2.2.3 on 2019-07-31 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20190731_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcel',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='Poids colis'),
        ),
    ]
