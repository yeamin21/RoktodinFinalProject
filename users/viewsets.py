from logging import log
import re
from django import http
from rest_framework import response, status, views, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.utils import serializer_helpers
from donation.models import BloodRequestResponse, Hospital
from donation.serializers import BloodRequestResponseSerializer
from users.models import Address, BloodGroup, Donor, RequestPhoneOrEmail, User
from users.serializers import AddressSerializer, BloodGroupSerializer, DonorSerializer, HospitalSerializer, RequestPhoneOrEmailSerializer, UserLocation, UserSerializer
from rest_framework import permissions
import geocoder
from geopy.geocoders import Nominatim

from rest_framework_simplejwt.tokens import RefreshToken


# from twilio.rest import messaging


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.id)
        serializer = self.get_serializer(user)
        return response.Response(serializer.data)
  
 
    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return response.Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    def create(self, request, *args, **kwargs):
        data=request.data
        data['user'] = request.user.id
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class DonorViewSet(viewsets.ModelViewSet):
    serializer_class = DonorSerializer
    queryset = Donor.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(is_donor=True )

    def create(self, request, *args, **kwargs):
        data=request.data
        data['user'] = request.user.id
        serializer = DonorSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def list(self, request, *args, **kwargs):
        serializer = DonorSerializer(self.get_queryset(),many=True,context={'request': request})
        return response.Response(serializer.data)

class BloodGroupViewSet(viewsets.ModelViewSet):
    serializer_class = BloodGroupSerializer
    queryset = BloodGroup.objects.all()

class RequestToCallOrEmailViewSet(viewsets.ModelViewSet):
    serializer_class = RequestPhoneOrEmailSerializer
    queryset = RequestPhoneOrEmail.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class UserLocationViewSet(views.APIView):
    def get(self, request):
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')
        geolocator = Nominatim(user_agent="roktodin")
        geolocator.geocode(query={'accept-language': 'en'}, language='en')
        if lat and lon:
            loc = geolocator.reverse(f'{lat}, {lon}')
        else:
            g = geocoder.ip('me')
            loc = geolocator.reverse(f'{g.latlng[0]}, {g.latlng[1]}')
            #location = UserLocation({'latitude': g.latlng[0], 'longitude': g.latlng[1]}).data
        return response.Response(loc.raw)


class HospitalViewSet(viewsets.ModelViewSet):
    serializer_class =HospitalSerializer
    queryset = Hospital.objects.all()