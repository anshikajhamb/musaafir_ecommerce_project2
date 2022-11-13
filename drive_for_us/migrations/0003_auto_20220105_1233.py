# Generated by Django 3.0.14 on 2022-01-05 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive_for_us', '0002_attachcar_car_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachcar',
            name='car_type',
            field=models.CharField(blank=True, choices=[('Hatchbacks and sedans', 'Hatchbacks and sedans'), ('SUV', 'SUV'), ('Tempo travellers', 'Tempo travellers')], max_length=50, null=True),
        ),
    ]