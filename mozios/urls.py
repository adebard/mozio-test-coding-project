from django.urls import include, path

from rest_framework import routers

from service_area import views


router = routers.DefaultRouter()
router.register(r'providers', views.ProviderViewSet, 'provider')
router.register(r'service-areas', views.ServiceAreaViewSet, 'service-area')


urlpatterns = [
    path('', include(router.urls))
]
