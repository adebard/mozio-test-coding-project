import json

from django.test import TestCase
from django.urls import reverse
from django.contrib.gis.geos import Polygon

from service_area.models import Provider, ServiceArea


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

    def test_provider_delete(self):
        self.assertEqual(Provider.objects.count(), 0)

        # NOTE: this can be improved using factoryboy.
        provider = Provider(name="Test", email="test@mail.com",
                           phone_number="1234")
        provider.save()

        self.assertEqual(Provider.objects.count(), 1)

        object_detail_url = reverse('provider-detail', args=[provider.id])
        response = self.client.delete(object_detail_url)

        self.assertEqual(Provider.objects.count(), 0)


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

    def test_post_service_areas_with_geojson_data(self):
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

    def test_post_service_areas_with_wkt_data(self):
        self.assertEqual(ServiceArea.objects.count(), 0)
        data = {
            "name": "Area for test",
            "price": "25",
            "area": "POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))",
            "provider": self.provider.id
        }
        response = self.client.post(self.service_areas, data=json.dumps(data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ServiceArea.objects.count(), 1)

    def test_search_service_areas_given_lat_long_pair(self):
        # NOTE: this can be improved using factoryboy.
        service_area = ServiceArea(
            name="Test",
            price="10",
            provider=self.provider,
            area=Polygon(((30.0, 10.0), (40.0, 40.0), (20.0, 40.0), (10.0, 20.0), (30.0, 10.0)))
        )
        service_area.save()

        search_url = self.service_areas + '?lat=35&long=30' # Query strings for search via lat/long pair.
        # This point must be contained in the previous service area created.
        response = self.client.get(search_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['id'], service_area.id) # The result should contain the service area created.

    def test_service_areas_delete(self):
        self.assertEqual(ServiceArea.objects.count(), 0)

        # NOTE: this can be improved using factoryboy.
        service_area = ServiceArea(
            name="Test",
            price="10",
            provider=self.provider,
            area=Polygon(((30.0, 10.0), (40.0, 40.0), (20.0, 40.0), (10.0, 20.0), (30.0, 10.0)))
        )
        service_area.save()

        self.assertEqual(ServiceArea.objects.count(), 1)

        object_detail_url = reverse('service-area-detail', args=[service_area.id])
        response = self.client.delete(object_detail_url)

        self.assertEqual(ServiceArea.objects.count(), 0)
