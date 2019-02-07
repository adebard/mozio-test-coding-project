import json

from django.test import TestCase
from django.urls import reverse

from service_area.models import Provider,ServiceArea


class TestProviders(TestCase):
    def setUp(self):
        self.providers_url = reverse('provider-list')

    def test_get_providers(self):
        response = self.client.get(self.providers_url)
        self.assertEqual(response.status_code, 200)

    def test_post_providers(self):
        self.assertEqual(Provider.objects.count(), 0)
        data = {
            "name": "Test",
            "email": "test@mail.com",
            "phone_number": "1234",
            "language": "US",
            "currency": "USD"
        }
        response = self.client.post(self.providers_url, data=json.dumps(data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Provider.objects.count(), 1)


class TestServiceArea(TestCase):
    def setUp(self):
        self.service_areas = reverse('service-area-list')
        # NOTE: this can be improved using factoryboy.
        provider = Provider(name="Test", email="test@mail.com",
                           phone_number="1234")
        provider.save()
        self.provider = provider

    def test_get_service_areas(self):
        response = self.client.get(self.service_areas)
        self.assertEqual(response.status_code, 200)

    def test_post_service_areas(self):
        self.assertEqual(ServiceArea.objects.count(), 0)
        data = {
            "name": "Area for test",
            "price": "25",
            "area": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [135.0, 45.0],
                        [140.0, 50.0],
                        [145.0, 55.0],
                        [135.0, 45.0]
                    ]
                ]
            },
            "provider": self.provider.id
        }
        response = self.client.post(self.service_areas, data=json.dumps(data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ServiceArea.objects.count(), 1)
