from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, TemplateView
from django.contrib.auth.models import User

from cars import forms, models
from cars.forms import RentCarForm


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


def car_rent_view(request, pk):
    car = models.Car.objects.get(pk=pk)
    form = RentCarForm(request.POST)
    if form.is_valid():
        car.is_rented = True
        car.save()
        return render(request, 'cars/car_rent_confirm.html')

    form = RentCarForm()
    return render(request, 'cars/car_rent.html', {'form': form})
