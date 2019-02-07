from django.contrib.gis.db import models


class Provider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    language = models.CharField(max_length=50, default='EN')
    currency = models.CharField(max_length=50, default='USD')

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    provider = models.ForeignKey(Provider,related_name='service_areas',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    area = models.PolygonField()

    def __str__(self):
        return '%s: %s' % (self.provider, self.name)
