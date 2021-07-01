from rest_framework import viewsets
from donation.models import Donation
from donation.serializers import DonationSerializer


class DonationViewSet(viewsets.ModelViewSet):
    serializer_class = DonationSerializer
    queryset = Donation.objects.all()
