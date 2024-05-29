# Generated by Django 5.0.6 on 2024-05-29 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido_p', models.CharField(max_length=100)),
                ('apellido_m', models.CharField(max_length=100)),
                ('fec_nac', models.DateField()),
                ('salario', models.IntegerField()),
                ('fec_contra', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]