from django.urls import path

from . import views

app_name = 'cars'

urlpatterns = [
    path('add_car/', views.add_car_view, name='add-car'),
]
