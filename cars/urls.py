from django.urls import path

from . import views

app_name = 'cars'

urlpatterns = [
    path('add_car/', views.AddCarView.as_view(), name='add-car'),
]
