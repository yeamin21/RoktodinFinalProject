from rest_framework import viewsets
from rest_framework.response import Response
from donation.models import Donation
from donation.serializers import DonationSerializer
from rest_framework.decorators import action


class DonationViewSet(viewsets.ModelViewSet):
    serializer_class = DonationSerializer
    queryset = Donation.objects.all()

    @action(methods=['GET'], detail=False, url_path='emergency', url_name='donation_emergency')
    def donation_emergency(self, request, **kwargs):
        _queryset = Donation.objects.filter(is_emergency=True)
        return Response(self.serializer_class(_queryset, many=True).data)
