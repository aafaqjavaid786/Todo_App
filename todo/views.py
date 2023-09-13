from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import RegistrationForm, TodoForm
from .models import ToDo
from django.urls import reverse_lazy

# Create your views here.


class UserRegistrationView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('add-todo')
    template_name = 'todo/index.html'


class TodoView(CreateView):
    form_class = TodoForm
    success_url = reverse_lazy('todo-list')
    template_name = 'todo/todo.html'

class TodoListView(ListView):
    model = ToDo
    template_name = 'todo/todo-list.html'
    context_object_name = 'todo_list'