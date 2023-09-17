from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .forms import RegistrationForm
from django.contrib.auth import login
from .models import Task
from django.urls import reverse_lazy

# Create your views here.


class UserRegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'todo/register.html'
    success_url = reverse_lazy('task-add')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class TaskAddView(CreateView):
    model = Task
    fields = ['title', 'description',]
    template_name = 'todo/task-add.html'
    success_url = reverse_lazy('task-list')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskListView(ListView):
    model = Task
    template_name = 'todo/task-list.html'

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)
    
class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo/task-detail.html'
    context_object_name = 'task'
    pk_url_kwarg = 'pk'

class TaskEditView(UpdateView):
    model = Task
    fields = ['title', 'description',]
    template_name = 'todo/task-edit.html'

    def get_success_url(self):
        return reverse_lazy('task-detail',args=(self.object.id,))
    
class TaskRemoveView(DeleteView):
    model = Task
    template_name = 'todo/task-remove.html'
    success_url = reverse_lazy('task-add')

    def get_success_url(self):
        if self.request.user != self.object.user:
            return reverse_lazy('all-tasks')
        else:
            return reverse_lazy('task-list')



class AllTasksView(ListView):
    model = Task
    template_name = 'todo/all-tasks.html'

    