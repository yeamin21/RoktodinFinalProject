from rest_framework import response, serializers, status, views
from twilio.rest import Client
from rest_framework import viewsets
from rest_framework.response import Response
from donation.models import BloodRequest, BloodRequestResponse, PhoneShareRequest
from donation.serializers import BloodRequestResponseSerializer, BloodRequestSerializer, PhoneShareRequestSerializer
from rest_framework.decorators import action, api_view
from users.models import Donor, User


class BloodRequestViewSet(viewsets.ModelViewSet):
    serializer_class = BloodRequestSerializer
    queryset = BloodRequest.objects.all()

    @action(methods=['GET'], detail=False, url_path='self_requests', url_name='blood_request_self')
    def self_requests(self, request, **kwargs):
        queryset = BloodRequest.objects.filter(receiver_id=request.user.id)
        return Response(self.serializer_class(queryset, many=True).data)

    def create(self, request, *args, **kwargs):
        blood_request = request.data
        blood_request['receiver'] = request.user.id
        print(request.data)
        serializer = BloodRequestSerializer(data=blood_request)
        if serializer.is_valid():
            self.perform_create(serializer)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        instance= self.get_object()
        updated_instance = BloodRequest.objects.get(id=instance.id)
        updated_instance.no_bag_managed= request.data.get('no_bag_managed')
        updated_instance.save()
        serializer = self.get_serializer(updated_instance)
        return Response(serializer.data)
    def get_queryset(self):
        is_emergency = bool(self.request.GET.get('is_emergency'))
        blood_group = self.request.GET.get('blood_group')
        query_dict={}
        if is_emergency==True:
            query_dict['is_emergency']=True
        if blood_group is not None:
            query_dict['blood_group']=blood_group
        return BloodRequest.objects.filter(**query_dict)
        
class PhoneShareRequestViewSet(viewsets.ModelViewSet):
    serializer_class = PhoneShareRequestSerializer
    queryset = PhoneShareRequest.objects.all()
    def get_queryset(self):
        return super().get_queryset().filter(receiver__user_id=self.request.user.id)
    
    def create(self, request, *args, **kwargs):
        account_sid = 'AC547bc494b43d6a0be0a094ded024b50a'
        auth_token = '025a796f0e52f657f2831ff4fd599a03'
        client = Client(account_sid, auth_token)
        receiver =  Donor.objects.get(user_id = request.data['receiver'])
        MSG_REQUEST_PHONE= 'You Have Received a Phone Number Sharing Request.\nPlease login to your ROKTODAN account and check.'
        PhoneShareRequest.objects.create(sender = request.user, receiver = receiver)
        client.messages.create(
            messaging_service_sid='MG2ee740e3452ae46afa8b88871e13b4a0',
            body=MSG_REQUEST_PHONE,
            to=receiver.phone.as_international,
            from_='+16816428342'
        )
        return response.Response({"message":'Created__OK'},status.HTTP_201_CREATED)

# @api_view(["POST"])  
# def sendSMS(request):
#     print(request.data)
#     if request.method=='POST':
        
        
#         return response.Response({'message':'Request Successfully Sent'}, status=status.HTTP_200_OK)


class BloodRequestResponseViewSet(viewsets.ModelViewSet):
    serializer_class = BloodRequestResponseSerializer
    queryset= BloodRequestResponse.objects.all()

    def create(self, request, *args, **kwargs):
        request_id = request.data.get('blood_request')
        blood_request = BloodRequest.objects.get(id=request_id)
        responder = Donor.objects.get(user_id=request.user.id)
        if blood_request.receiver == request.user:
            return response.Response({'You Cant Respond to Your Own Request'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = BloodRequestResponseSerializer(data={'blood_request':request_id , 'respondent':responder.id})
            if serializer.is_valid():
                self.perform_create(serializer)
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)
            print(serializer.errors)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get('request_id'):
            queryset = queryset.filter(blood_request_id=self.request.GET.get('request_id'))
        return queryset
    # def get_queryset(self):

        #return BloodRequestResponse.objects.filter(bl ood_request_id=self.request.GET.get('request_id'))

    def update(self, request, *args, **kwargs):
        print('cxafsafas')
        return super().update(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        instance= self.get_object()
        updated_instance = BloodRequestResponse.objects.get(id=instance.id)
        print(instance)
        updated_instance.fullfilled= request.data.get('fullfilled')
        updated_instance.save()
        serializer = self.get_serializer(updated_instance)
        return Response(serializer.data)