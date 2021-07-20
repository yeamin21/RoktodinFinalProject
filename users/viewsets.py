from rest_framework import response, viewsets
from users.models import User
from users.serializers import UserSerializer
from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        serializer = self.get_serializer(user)
        return response.Response(serializer.data)
