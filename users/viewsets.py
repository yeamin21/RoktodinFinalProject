from rest_framework import response, viewsets
from users.models import Donor, User
from users.serializers import DonorSerializer, UserSerializer
from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        serializer = self.get_serializer(user)
        return response.Response(serializer.data)

class DonorViewSet(viewsets.ModelViewSet):
    serializer_class = DonorSerializer
    queryset = Donor.objects.all()