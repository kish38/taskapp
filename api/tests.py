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

    def test_create_tasks(self):
        req = self.client.post(reverse('list-tasks'), data={'name': 'New Task'})
        self.assertEqual(req.status_code, 201)
        tasks = Task.objects.count()
        self.assertEqual(tasks, 3)

    def test_get_a_task(self):
        task = Task.objects.first()
        req = self.client.get(reverse('get-task', args=[task.id]))
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.data['name'], task.name)

    def test_update_a_task(self):
        task = Task.objects.first()
        req = self.client.patch(reverse('get-task', args=[task.id]), data={'name': 'First task'})
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.data['name'], 'First task')

    def test_delete_a_task(self):
        task = Task.objects.first()
        req = self.client.delete(reverse('get-task', args=[task.id]))
        self.assertEqual(req.status_code, 204)
        self.assertEqual(1, Task.objects.count())
