from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework  import viewsets
from rest_framework.authtoken.models import Token
from rest_framework import (generics, permissions, status)
from rest_framework.permissions import IsAdminUser
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import (Investor, BusinessOwner, Business, BlockedUser)
from .serializers import (AuthorizationSerializer, UserSerializer, 
                         BusinessSerializer, BusinessOwnerSerializer, InvestorSerializer)


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




# class UserListView(generics.ListCreateAPIView):
#     permission_classes = [IsAdminUser]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAdminUser]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class BusinessListView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class BusinessDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user:
            return Response(status=403)
        self.perform_destroy(instance)
        return Response(status=204)



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



class BusinessPremiumView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_premium = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



# class BusinessDetailView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAdminUser]
#     queryset = Business.objects.all()
#     serializer_class = BusinessSerializer





class InvestorListView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer


class InvestorDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer


class BusinessOwnerViewSet(viewsets.ModelViewSet):
    queryset = BusinessOwner.objects.all()
    serializer_class = BusinessOwnerSerializer

    @action(detail=True)
    def bus(self, request, pk=None):
        business_owner = self.get_object()
        bus = Business.objects.filter(owner=business_owner)
        serializer = BusinessSerializer(bus, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def toggle_bus_status(self, request, pk=None):
        business_owner = self.get_object()
        bus = Business.objects.get(pk=request.data['bus_id'], owner=business_owner)
        bus.is_active = not bus.is_active
        bus.save()
        serializer = BusinessSerializer(bus)
        return Response(serializer.data)










