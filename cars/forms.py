from django import forms


class RentCarForm(forms.Form):

    days = forms.IntegerField()

