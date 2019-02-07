from rest_framework import serializers

from service_area.models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ServiceAreaSerializer(serializers.ModelSerializer):
    provider_name = serializers.SerializerMethodField()

    def get_provider_name(self, obj):
        return obj.provider.name

    class Meta:
        model = ServiceArea
        fields = '__all__'
