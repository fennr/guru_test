from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework_extensions.mixins import NestedViewSetMixin

from django_filters import rest_framework as df

from service import models, serializers, filters


class CityViewSet(viewsets.ModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer


class StreetViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = models.Street.objects.all()
    serializer_class = serializers.StreetSerializer


class ShopListCreateAPIView(ListCreateAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer
    filter_backends = [df.DjangoFilterBackend]
    filterset_class = filters.ShopFilter

    def perform_create(self, serializer):
        serializer.save(city_id=self.request.data['city_id'], street_id=self.request.data['street_id'])

