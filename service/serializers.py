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
    # street = serializers.SlugRelatedField(read_only=True, slug_field='name')
    # city = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = models.Shop
        fields = "__all__"