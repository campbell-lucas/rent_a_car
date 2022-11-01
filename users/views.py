from django.shortcuts import render, reverse
from django.views.generic import FormView
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
