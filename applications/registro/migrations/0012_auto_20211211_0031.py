# Generated by Django 3.2.7 on 2021-12-11 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0011_auto_20211211_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='materia',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='registro.materia'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='oficina',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='registro.oficina'),
        ),
    ]
