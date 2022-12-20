# Generated by Django 4.1.2 on 2022-12-20 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0009_car_renter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='renter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_renter', to=settings.AUTH_USER_MODEL),
        ),
    ]
