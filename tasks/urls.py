from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.get_tasks),
    path('tasks/add/', views.add_task),
    path('tasks/<int:task_id>/complete/', views.complete_task),
]