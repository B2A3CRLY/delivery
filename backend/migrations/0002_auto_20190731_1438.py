# Generated by Django 2.2.3 on 2019-07-31 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date Creation Livraison'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='date_livraison',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date Livraison'),
        ),
    ]
