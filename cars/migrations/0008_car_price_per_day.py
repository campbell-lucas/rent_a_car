# Generated by Django 4.1.2 on 2022-11-23 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_car_location_delete_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price_per_day',
            field=models.PositiveIntegerField(default=100),
        ),
    ]
