# Generated by Django 2.1.2 on 2018-10-27 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20181026_2311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascota',
            old_name='Estado',
            new_name='estado',
        ),
    ]
