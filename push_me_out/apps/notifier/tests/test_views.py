from django.urls import reverse
from rest_framework.test import APITestCase

from apps.notifier.models import Subscriber


class SubscribersViewTestCase(APITestCase):
    def test_success_creation(self):
        request = {
            'service_endpoint': 'http://www.test.com',
            'p256dh': 'test_p256dh',
            'auth': 'test_auth'
        }

        self.assertEqual(Subscriber.objects.count(), 0)
        with self.assertNumQueries(2):
            # 1. Check if endpoint already exists
            # 2. Insert endpoint
            url = reverse('subscribers_view')
            response = self.client.post(path=url, data=request, format='json')

        self.assertEqual(Subscriber.objects.count(), 1)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['service_endpoint'], 'http://www.test.com')

    def test_bad_request(self):
        request = {
            'service_endpoint': 'http://www.test.com',
            'p256dh': 'test_p256dh',
            'auth': 'test_auth'
        }
        url = reverse('subscribers_view')

        self.assertEqual(Subscriber.objects.count(), 0)
        with self.assertNumQueries(2):
            # 1. Check if endpoint already exists
            # 2. Insert endpoint
            response = self.client.post(path=url, data=request, format='json')

        self.assertEqual(Subscriber.objects.count(), 1)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['service_endpoint'], 'http://www.test.com')

        with self.assertNumQueries(1):
            # 1. Check if endpoint already exists
            response = self.client.post(path=url, data=request, format='json')

        self.assertEqual(Subscriber.objects.count(), 1)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['service_endpoint'][0], 'subscriber with this service endpoint already exists.')
