from django import template
from cars.models import Car

register = template.Library()


@register.filter(name='my_rented_cars')
def my_rented_cars(user, user_pk):
    rented_car = Car.objects.get(renter=user_pk)
    return True if rented_car in Car.objects.all() else False
