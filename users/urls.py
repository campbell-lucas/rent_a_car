from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/my-cars/', views.MyCars.as_view(), name='my-cars'),
    path('profile/my-cars/return/', views.return_car, name='return-car'),
]
