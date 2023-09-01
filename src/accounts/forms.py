from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = [
            'email',
            'phone_number',
            'password1',
            'password2'
        ]

