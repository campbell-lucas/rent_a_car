from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('search/', views.SearchResultsView.as_view(), name='car-search'),
]