from django.urls import path
from api.views import ListTasks


urlpatterns = [
    path('tasks/', ListTasks.as_view(), name='list-tasks'),
]
