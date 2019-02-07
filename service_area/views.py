from django.contrib.gis.geos import Point

from rest_framework import viewsets

from service_area.serializers import ProviderSerializer, ServiceAreaSerializer
from service_area.models import Provider, ServiceArea


class ProviderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows providers to be created, viewed or edited.
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows service areas to be created, viewed, or edited.
    Also allows to search service areas given a latitude and longitude.
    """
    serializer_class = ServiceAreaSerializer

    def get_queryset(self):
        queryset = ServiceArea.objects.all()

        lat = self.request.query_params.get('lat', None)
        long = self.request.query_params.get('long', None)

        if lat and long:
            point = Point(float(lat), float(long))
            queryset = queryset.filter(area__contains=point)

        return queryset
