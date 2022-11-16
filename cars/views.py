from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
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


# def add_car_view(request):
#     form = forms.AddCarForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             car = form.save(commit=False)
#             car.save()
#             return redirect(reverse_lazy('users:profile'))
#     return render(request, 'cars/add_car.html', {'form': form})
