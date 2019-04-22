# Generated by Django 2.2 on 2019-04-21 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='', max_length=100)),
                ('Size', models.CharField(default='None', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Apartments',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.CharField(default='None', max_length=100)),
                ('LGA', models.CharField(default='None', max_length=100)),
                ('District', models.CharField(default='None', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='RentPerMonth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('range', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'PriceRangesPerMonth',
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(default='', max_length=100)),
                ('Last_Name', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Tenants',
            },
        ),
        migrations.CreateModel(
            name='TenantDecision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Apartment_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenant.Apartments')),
                ('Location_of_Choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenant.Location')),
                ('Price_Range', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenant.RentPerMonth')),
            ],
            options={
                'verbose_name_plural': 'TenantDecisions',
            },
        ),
        migrations.AddField(
            model_name='apartments',
            name='Choice_of_Location',
            field=models.ForeignKey(default='Lagos', on_delete=django.db.models.deletion.CASCADE, to='tenant.Location'),
        ),
    ]
