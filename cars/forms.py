from django import forms
from .models import Car

#
# class AddCarForm(forms.ModelForm):
#
#     class Meta:
#         model = Car
#         fields = ('car_brand', 'car_model', 'car_color', 'number_of_seats', 'number_of_doors', 'category')
#
#     def save(self, commit=True):
#         car = super().save(commit=True)
#         return car
