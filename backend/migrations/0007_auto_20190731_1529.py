# Generated by Django 2.2.3 on 2019-07-31 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20190731_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcel',
            name='status',
            field=models.CharField(choices=[('Livré', 'Livré'), ('En attente de collecte', 'En attente de collecte'), ('Avec le livreur', 'Avec le livreur'), ('Avec la société de livraison', 'Avec la société de livraison')], default='En attente de collecte', max_length=50, verbose_name='Status colis'),
        ),
    ]
