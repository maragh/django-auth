from django.contrib.auth import authenticate, login
from django import forms
from django_auth.models import User


class LoginForm(forms.Form):
    email = forms.CharField(
        required=True,
        max_length=100,
        label='',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control mb-4',
                'placeholder': 'johndoe@gmail.com'
            }
        )
    )
    password = forms.CharField(
        required=True,
        max_length=100,
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mb-4',
                'placeholder': 'password'
            }
        )
    )

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid.")
        return self.cleaned_data

    def login(self, request):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        return user

