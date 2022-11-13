# Generated by Django 3.0.14 on 2022-01-05 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporate', '0005_companysignup_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addemployees',
            name='company_name',
            field=models.TextField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='addemployees',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='addemployees',
            name='name',
            field=models.TextField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='addemployees',
            name='password',
            field=models.TextField(blank=True, max_length=80, null=True),
        ),
    ]