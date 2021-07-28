from twilio.rest import Client
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


def send():
    account_sid = 'AC547bc494b43d6a0be0a094ded024b50a'
    auth_token = '025a796f0e52f657f2831ff4fd599a03'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid='MG2ee740e3452ae46afa8b88871e13b4a0',
        body='Hello Received a request',
        to='+8801954492600'
    )

    print(message.sid)
