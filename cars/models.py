import django.contrib.auth.models
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Car(models.Model):
    car_brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_color = models.CharField(max_length=100)
    number_of_seats = models.CharField(max_length=100)
    number_of_doors = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='car_category')
    owner = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE, related_name='car_owner')

    def __str__(self):
        return self.car_model

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
