from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('register', views.UserRegistrationView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('task/add', views.TodoView.as_view(), name='add-task'),
    path('task/list', views.TodoListView.as_view(), name='task-list'),
]
