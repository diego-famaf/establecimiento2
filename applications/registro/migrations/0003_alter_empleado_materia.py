# Generated by Django 3.2.7 on 2021-10-14 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_empleado_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.materia'),
        ),
    ]