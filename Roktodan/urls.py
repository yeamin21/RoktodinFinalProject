"""FinPr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from users.models import User
from users.viewsets import AddressViewSet, BloodGroupViewSet, DonorViewSet, HospitalViewSet, RequestToCallOrEmailViewSet, UserLocationViewSet, UserViewSet
from donation.viewsets import BloodRequestResponseViewSet, BloodRequestViewSet, PhoneShareRequestViewSet
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register('requests', BloodRequestViewSet)
router.register('users', UserViewSet)
router.register('donors', DonorViewSet)
router.register('notify', RequestToCallOrEmailViewSet)
router.register('bloodgroups', BloodGroupViewSet)
router.register('addresses', AddressViewSet)
router.register('share_requests',PhoneShareRequestViewSet)
router.register('responses',BloodRequestResponseViewSet)
router.register('hospitals',HospitalViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/users/', UserViewSet.as_view(), name='get_allUser'),
    path('api/user/', UserViewSet.as_view({'get': 'retrieve'}), name='get_user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('api/user-location/', UserLocationViewSet.as_view()),
 
]
