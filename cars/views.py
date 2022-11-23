from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView
from django.contrib.auth.models import User

from cars import forms, models


class AddCarView(CreateView):

    model = models.Car
    fields = [
        'car_brand',
        'car_model',
        'car_color',
        'number_of_seats',
        'number_of_doors',
        'category',
        'owner',
        'location',
        'price_per_day',
    ]

    template_name = 'cars/add_car.html'
    raise_exception = False
    success_url = reverse_lazy('home:home')

    def get_form(self, *args, **kwargs):
        form = super(AddCarView, self).get_form(*args, **kwargs)
        form.fields['owner'].queryset = User.objects.all().filter(username=self.request.user.username)
        return form

    def form_valid(self, form):
        return super().form_valid(form)


class CarProfileView(DetailView):

    model = models.Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CarRentView(TemplateView):
    pass
