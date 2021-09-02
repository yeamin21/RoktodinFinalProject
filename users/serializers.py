from django.db.models import fields
from geocoder.api import postal
from rest_framework import serializers
from users.models import Donor, RequestPhoneOrEmail, User


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = '__all__'

    def to_representation(self, instance):
        if not instance.share_phone:
            instance.phone = None
        return super().to_representation(instance)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class RequestPhoneOrEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestPhoneOrEmail
        fields = '__all__'


class UserLocation(serializers.Serializer):
    latitude = serializers.DecimalField(max_digits=10, decimal_places=8)
    longitude = serializers.DecimalField(max_digits=11, decimal_places=8)
    # city
    # country
    # postal
    # road
    # country_code
