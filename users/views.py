from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import (generics, permissions, status)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer
from .serializers import AuthorizationSerializer



class Authorization(TokenObtainPairView):
    serializer_class = AuthorizationSerializer



class RegisterAPI(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        user_serializer = self.serializer_class(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key})



class UserAPI(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user



from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import User, Business, Advertisement
from .serializers import UserSerializer, BusinessSerializer, AdvertisementSerializer

class UserListView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BusinessListView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class BusinessDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class AdvertisementListView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

class AdvertisementDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

class AdvertisementPremiumView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_premium = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class UserBlockView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)





