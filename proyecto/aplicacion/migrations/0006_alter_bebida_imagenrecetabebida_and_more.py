# Generated by Django 5.0.2 on 2024-03-27 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0005_alter_bebida_imagenrecetabebida_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bebida',
            name='imagenRecetaBebida',
            field=models.ImageField(blank=True, null=True, upload_to='static/galeria'),
        ),
        migrations.AlterField(
            model_name='dulce',
            name='imagenRecetaDulce',
            field=models.ImageField(blank=True, null=True, upload_to='static/galeria'),
        ),
        migrations.AlterField(
            model_name='salada',
            name='imagenRecetaSalada',
            field=models.ImageField(blank=True, null=True, upload_to='static/galeria'),
        ),
    ]