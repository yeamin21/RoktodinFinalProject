from logging import log
from django import http
from rest_framework import response, views, viewsets
from users.models import Donor, RequestPhoneOrEmail, User
from users.serializers import DonorSerializer, RequestPhoneOrEmailSerializer, UserLocation, UserSerializer
from rest_framework import permissions
import geocoder
from geopy.geocoders import Nominatim
# from twilio.rest import messaging


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        serializer = self.get_serializer(user)
        return response.Response(serializer.data)


class DonorViewSet(viewsets.ModelViewSet):
    serializer_class = DonorSerializer
    queryset = Donor.objects.all()


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
