# Generated by Django 5.1 on 2024-08-31 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='calcData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('Vehicle_Class', models.CharField(max_length=255)),
                ('Engine_Size', models.IntegerField()),
                ('Cylinder', models.IntegerField()),
                ('Transmission', models.CharField(max_length=255)),
                ('Fuel_Type', models.CharField(max_length=255)),
                ('Fuel_Consumption', models.CharField(max_length=255)),
            ],
        ),
    ]
