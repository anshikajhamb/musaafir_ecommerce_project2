# Generated by Django 3.0.14 on 2022-01-07 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corporate', '0008_addemployees_updated_budget'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addemployees',
            name='password',
        ),
    ]