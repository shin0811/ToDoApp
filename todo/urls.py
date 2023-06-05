"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from todo.views import TaskListView, TaskDetailView, TaskCreatView, TaskDeleteView, TaskUpdateView

urlpatterns = [
    path("", TaskListView.as_view(), name = "task-list"),
    path("task/new/", TaskCreatView.as_view(), name = "task-new"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name = "task-detail"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name = "task-delete"),
    path("task/<int:pk>/edit/", TaskUpdateView.as_view(), name = "task-edit"),
]
