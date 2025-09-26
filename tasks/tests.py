from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Task


class TaskModelTest(TestCase):
    """Test cases for Task model"""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )

    def test_task_creation(self):
        """Test creating a task"""
        task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            priority="high",
            assigned_to=self.user,
        )
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.status, "todo")  # default status
        self.assertEqual(task.priority, "high")
        self.assertEqual(task.assigned_to, self.user)

    def test_task_str_method(self):
        """Test task string representation"""
        task = Task.objects.create(title="Test Task", assigned_to=self.user)
        self.assertEqual(str(task), "Test Task")


class TaskAPITest(APITestCase):
    """Test cases for Task API endpoints"""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )
        self.task_data = {
            "title": "Test API Task",
            "description": "Test API Description",
            "priority": "medium",
            "status": "todo",
        }

    def test_create_task(self):
        """Test creating task via API"""
        self.client.force_authenticate(user=self.user)
        url = reverse("task-list")
        response = self.client.post(url, self.task_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, "Test API Task")

    def test_get_task_list(self):
        """Test retrieving task list"""
        Task.objects.create(**self.task_data)
        url = reverse("task-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_get_task_detail(self):
        """Test retrieving single task"""
        task = Task.objects.create(**self.task_data)
        url = reverse("task-detail", kwargs={"pk": task.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test API Task")

    def test_update_task(self):
        """Test updating task via API"""
        self.client.force_authenticate(user=self.user)
        task = Task.objects.create(**self.task_data)
        url = reverse("task-detail", kwargs={"pk": task.pk})
        updated_data = {"title": "Updated Task Title", "status": "completed"}
        response = self.client.patch(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.title, "Updated Task Title")
        self.assertEqual(task.status, "completed")

    def test_delete_task(self):
        """Test deleting task via API"""
        self.client.force_authenticate(user=self.user)
        task = Task.objects.create(**self.task_data)
        url = reverse("task-detail", kwargs={"pk": task.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
