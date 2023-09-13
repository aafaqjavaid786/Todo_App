from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ToDo

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']


class TodoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'desc', 'user']
        labels = {
            'title': 'Title',
            'desc': 'Description',
            'user': 'User'
        }
