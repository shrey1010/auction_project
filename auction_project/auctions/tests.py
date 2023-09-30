from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Auction
from accounts.models import CustomUser


class AuctionTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.admin = CustomUser.objects.create_superuser(
            'admin', 'admin@admin.com', '<admin_password>')
        self.client.force_authenticate(user=self.admin)

    def test_create_auction(self):
        url = reverse('auction-list')
        data = {'start_time': '2023-10-01T12:00:00Z', 'end_time': '2023-10-01T14:00:00Z',
                'start_price': '100.00', 'item_name': 'Test Item'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Auction.objects.count(), 1)

    def test_get_auction_list(self):
        url = reverse('auction-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_auction_detail(self):
        auction = Auction.objects.create(start_time='2023-10-01T12:00:00Z',
                                         end_time='2023-10-01T14:00:00Z',
                                         start_price='100.00',
                                         item_name='Test Item')
        url = reverse('auction-detail', args=[auction.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more tests as needed
