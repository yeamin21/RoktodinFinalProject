from django.db import models
from django.db.models import fields
from geocoder.api import postal
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from donation.models import Hospital
from users.models import Address, BloodGroup, Donor, RequestPhoneOrEmail, User
import datetime
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from geopy import Nominatim, distance
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields ='__all__'

    
class DonorSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')  
    blood_type = serializers.ReadOnlyField(source='blood_group.type')
    blood_factor = serializers.ReadOnlyField(source='blood_group.get_factor_display')
   
    able_to_donate = serializers.ReadOnlyField()
    distance = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Donor
        fields = ['user','first_name','last_name','blood_group','blood_type','blood_factor','is_donor','able_to_donate',
        'last_donation','phone', 'share_phone','distance','city']
        # extra_kwargs = {
        #     'blood_group':{'write_only': True},
        # }
    def get_distance(self,object):
        request = self.context.get("request")
        try:
            address = Address.objects.get(user_id=object.user.id)  
            lat = request.GET.get('lat')
            lon = request.GET.get('lon')
            if lat and lon:
                d = distance.distance
                g = Nominatim(user_agent="roktodan_loc")
                wa = (lat,lon)
                _, pa = g.geocode(f'{address.address}, {address.city}, {address.postcode}')
                return round((d(wa, pa).kilometers),1)
            else:
                return None
        except:
            return None
        
    def get_city(self,obj):
        try:
            address = Address.objects.get(user_id=obj.user.id)  
            return address.city
        except:
            return None

    def to_representation(self, instance):
        if not instance.share_phone:
            instance.phone = None
        if  instance.last_donation is not None and (instance.last_donation - datetime.date.today()).days < 120:
            instance.able_to_donate = False
        else:
            instance.able_to_donate = True
        return super().to_representation(instance)

class BloodGroupSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = BloodGroup
        fields=['id', 'name']
    def get_name(self,obj):
        return f'{obj.get_type_display()}{obj.get_factor_display()}'


 
class UserSerializer(serializers.ModelSerializer):
    donor_details = DonorSerializer(required=False,read_only=True)
    user_address = AddressSerializer(required=False)
    user_phone =serializers.SerializerMethodField()
    #password=serializers.CharField(write_only=True)
    class Meta:
        model = get_user_model()
        fields = ['id','username', 'first_name', 'last_name','user_phone','password', 'email', 'donor_details', 'user_address']
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    def get_user_phone(self,obj):
        try:
            phone = obj.donor_details.phone.as_national
        except:
            phone = None
        return phone
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
class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields='__all__'