from rest_framework import serializers

from service import models


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.City
        fields = "__all__"


class StreetSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Street
        fields = "__all__"


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Shop
        fields = "__all__"