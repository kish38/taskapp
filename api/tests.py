from django.urls import reverse
from django.test import TestCase
from api.models import Task


class BasicTests(TestCase):

    def test_home(self):
        req = self.client.get(reverse('home'))
        self.assertEqual(req.status_code, 200)


class TaskAPITests(TestCase):

    def setUp(self):
        Task.objects.create(name="Task one")
        Task.objects.create(name="Task two")

    def test_model_create(self):
        tasks = Task.objects.count()
        self.assertEqual(tasks, 2)
        task = Task.objects.create(name="Third task")
        self.assertEqual(Task.objects.count(), 3)
        self.assertEqual(task.completed, False)
