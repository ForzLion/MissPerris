# Generated by Django 2.1.2 on 2018-10-25 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181025_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='imagen',
            field=models.ImageField(upload_to='photo'),
        ),
    ]
