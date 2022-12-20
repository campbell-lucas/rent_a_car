from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse
from django.views.generic import FormView, ListView

from cars.models import Car
from . import forms


class SignupView(FormView):
    form_class = forms.RegistrationForm
    template_name = 'users/signup.html'
    success_url = '/'

    def form_valid(self, form):
        if form.is_valid():
            user = form.save(commit=True)
            user.is_active = True
            user.save()
        return super().form_valid(form)


@login_required
def profile_view(request):
    return render(request, 'users/profile.html')


class MyCars(ListView):
    model = Car
    template_name = 'users/users_cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.filter(renter=self.request.user.pk)


def return_car(request):
    car = Car.objects.get(renter=request.user.pk)
    car.is_rented = False
    car.renter = None
    car.save()
    return render(request, 'cars/car_return_confirm.html')
