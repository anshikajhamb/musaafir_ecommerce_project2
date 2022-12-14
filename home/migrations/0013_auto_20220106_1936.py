# Generated by Django 3.0.14 on 2022-01-06 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20220106_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='citycabbooking',
            name='cabname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.CityCab'),
        ),
        migrations.AddField(
            model_name='citycabbooking',
            name='destination',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='citycabbooking',
            name='pickup',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='citycabbooking',
            name='pickup_datetime',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='FilteringHistory',
        ),
    ]
