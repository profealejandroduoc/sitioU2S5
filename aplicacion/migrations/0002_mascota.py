# Generated by Django 4.2.1 on 2023-05-23 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=25)),
                ('nombre', models.CharField(max_length=50)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aplicacion.persona')),
            ],
        ),
    ]