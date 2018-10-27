# Generated by Django 2.1.2 on 2018-10-25 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chip', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('fechaI', models.DateField()),
                ('fechaNac', models.DateField()),
                ('descripcion', models.TextField(max_length=300)),
                ('imagen', models.ImageField(upload_to='')),
                ('Estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Estado')),
            ],
            options={
                'verbose_name': 'Mascota',
                'verbose_name_plural': 'Mascotas',
            },
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Raza',
                'verbose_name_plural': 'Razas',
            },
        ),
        migrations.AlterModelOptions(
            name='ciudad',
            options={'verbose_name': 'Ciudad', 'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='comuna',
            options={'verbose_name': 'Comuna', 'verbose_name_plural': 'Comunas'},
        ),
        migrations.AlterModelOptions(
            name='persona',
            options={'verbose_name': 'persona', 'verbose_name_plural': 'personas'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'Region', 'verbose_name_plural': 'Regiones'},
        ),
        migrations.AlterModelOptions(
            name='vivienda',
            options={'verbose_name': 'Vivienda', 'verbose_name_plural': 'Viviendas'},
        ),
        migrations.AlterField(
            model_name='persona',
            name='rut',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='raza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Raza'),
        ),
    ]
