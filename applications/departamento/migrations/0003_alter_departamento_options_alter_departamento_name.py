# Generated by Django 4.1.6 on 2023-02-16 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_alter_departamento_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['name'], 'verbose_name': 'Mi Departamento', 'verbose_name_plural': 'Areas de la empresa'},
        ),
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Nombre'),
        ),
    ]
