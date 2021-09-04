from django.db.models import fields
from geocoder.api import postal
from rest_framework import serializers
from users.models import Address, Donor, RequestPhoneOrEmail, User


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ['blood_group', 'phone', 'share_phone']

    def to_representation(self, instance):
        if not instance.share_phone:
            instance.phone = None
        return super().to_representation(instance)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['address_line_1', 'address_line_2', 'city', 'district', 'division', 'postal', 'country']


class UserSerializer(serializers.ModelSerializer):
    donor_details = DonorSerializer(required=False)
    user_address = AddressSerializer(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'donor_details', 'user_address']


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
