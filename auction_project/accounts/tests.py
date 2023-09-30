from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import CustomUser


class CustomUserTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.admin = CustomUser.objects.create_superuser(
            'admin', 'admin@admin.com', '<admin_password>')
        self.client.force_authenticate(user=self.admin)

    def test_create_user(self):
        url = reverse('user-list')
        data = {'username': 'testuser',
                'email': 'test@test.com', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 2)

    def test_get_user_list(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_detail(self):
        user = CustomUser.objects.create_user(
            'testuser', 'test@test.com', 'testpassword')
        url = reverse('user-detail', args=[user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more tests as needed
