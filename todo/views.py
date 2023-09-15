from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task
from django.urls import reverse_lazy

# Create your views here.


class UserRegistrationView(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('add-task')
    template_name = 'todo/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class TodoView(CreateView):
    model = Task
    fields = ['title', 'description',]
    success_url = reverse_lazy('task-list')
    template_name = 'todo/add-task.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TodoListView(ListView):
    model = Task
    template_name = 'todo/task-list.html'
    context_object_name = 'task_list'

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)
    