from django.urls import path
from . import views

urlpatterns = [
    path('register', views.UserRegistrationView.as_view(), name='register-user'),
    path('todo', views.TodoView.as_view(), name='add-todo'),
    path('todo/list', views.TodoListView.as_view(), name='todo-list'),
]
