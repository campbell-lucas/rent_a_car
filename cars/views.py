from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from cars import forms


def add_car_view(request):
    form = forms.AddCarForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect(reverse_lazy('users:profile'))
    return render(request, 'cars/add_car.html', {'form', form})
