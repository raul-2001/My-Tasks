from django.test import TestCase
from django.urls import path
from  .views import *

urlpatterns = [
    path('', index, name = 'list'),
    path('update_task/<int:task_id>/', update_task, name='my_update_task'),
    path('delete/<int:task_id>/', delete_tasks, name='delete')
]
