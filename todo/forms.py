from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task
from django_summernote.widgets import SummernoteWidget

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','is_staff']
        labels = {
            'is_staff': 'Is Admin?'
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description',]
        widgets = {'description': SummernoteWidget()}
    
