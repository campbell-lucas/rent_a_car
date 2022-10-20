from django.shortcuts import render
from django.views.generic import FormView
from . import forms


def login_view(request):
    return render(request, 'users/login.html')


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
