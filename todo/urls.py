from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('task/add/', views.TaskAddView.as_view(), name='task-add'),
    path('task/list/', views.TaskListView.as_view(), name='task-list'),
    path('task/all/', views.AllTasksView.as_view(),name='all-tasks'),
    path('task/<str:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('task/<str:pk>/edit/', views.TaskEditView.as_view(), name='task-edit'),
    path('task/<str:pk>/remove/', views.TaskRemoveView.as_view(), name='task-remove'),
    path('update-task-order/', views.UpdateTaskOrderView.as_view(), name='update-task-order'),
]