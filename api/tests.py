from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from api.models import Task
from api.serializers import TaskSerializer


class BasicTests(TestCase):

    def test_home(self):
        req = self.client.get(reverse('home'))
        self.assertEqual(req.status_code, 200)


class TaskModelTests(TestCase):

    def setUp(self):
        Task.objects.create(name="Task one")
        Task.objects.create(name="Task two")

    def test_model_create(self):
        tasks = Task.objects.count()
        self.assertEqual(tasks, 2)
        task = Task.objects.create(name="Third task")
        self.assertEqual(Task.objects.count(), 3)
        self.assertEqual(task.completed, False)


class TaskAPITests(APITestCase):

    def setUp(self):
        Task.objects.create(name="Task one")
        Task.objects.create(name="Task two")

    def test_list_tasks(self):
        tasks = Task.objects.all()
        serialized = TaskSerializer(tasks, many=True)
        req = self.client.get(reverse('list-tasks'))
        self.assertEqual(req.status_code, 200)
        self.assertEqual(serialized.data, req.data)
