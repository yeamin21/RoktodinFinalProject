from rest_framework import viewsets
from rest_framework.response import Response
from donation.models import BloodRequest
from donation.serializers import BloodSerializer
from rest_framework.decorators import action


class BloodRequestViewSet(viewsets.ModelViewSet):
    serializer_class = BloodSerializer
    queryset = BloodRequest.objects.all()

    @action(methods=['GET'], detail=False, url_path='emergency', url_name='request_emergency')
    def request_emergency(self, request, **kwargs):
        _queryset = BloodRequest.objects.filter(is_emergency=True)
        return Response(self.serializer_class(_queryset, many=True).data)
