from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from api.serializers import TaskSerializer
from api.serializers import SingleTaskSerializer
from api.models import Task


def home_page(request):
    return HttpResponse("Task App Home")


class ListTasks(ListCreateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class GetTask(RetrieveUpdateDestroyAPIView):

    queryset = Task.objects.all()
    serializer_class = SingleTaskSerializer
