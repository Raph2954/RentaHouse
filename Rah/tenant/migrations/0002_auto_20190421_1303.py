# Generated by Django 2.2 on 2019-04-21 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartments',
            name='Choice_of_Location',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='tenant.Location'),
        ),
    ]
