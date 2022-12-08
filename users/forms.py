from django import forms
from django.contrib.auth import get_user_model


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')
        help_texts = {
            'username': None,
            'email': None,
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))

        if commit:
            user.save()

        return user
