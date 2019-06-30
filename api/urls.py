from django.urls import path
from api.views import ListTasks
from api.views import GetTask


urlpatterns = [
    path('tasks/', ListTasks.as_view(), name='list-tasks'),
    path('tasks/<int:pk>', GetTask.as_view(), name='get-task')
]
