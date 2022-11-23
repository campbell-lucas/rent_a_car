from django.urls import path

from . import views

app_name = 'cars'

urlpatterns = [
    path('add_car/', views.AddCarView.as_view(), name='add-car'),
    path('car_profile/<int:pk>/', views.CarProfileView.as_view(), name='car-profile'),
    path('rent_car/<int:pk>/', views.CarRent.as_view(), name='car_rent'),
]
