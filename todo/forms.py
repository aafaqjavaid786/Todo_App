from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    # is_admin = forms.BooleanField()

    class Meta:
        model = User
        fields = ['username','is_staff']
        labels = {
            'is_staff': 'Is Admin?'
        }