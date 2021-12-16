# Generated by Django 3.2.7 on 2021-12-11 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0012_auto_20211211_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='materia',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.materia'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='oficina',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.oficina'),
        ),
    ]