# Generated by Django 2.2.3 on 2019-08-01 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_auto_20190801_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivery',
            old_name='parcel',
            new_name='parcels',
        ),
    ]
