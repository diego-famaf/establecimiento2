# Generated by Django 3.2.7 on 2021-10-14 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_alter_empleado_oficina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='oficina',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='registro.oficina'),
        ),
    ]
