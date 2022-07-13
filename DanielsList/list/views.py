from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .serializers import RingSerializer, UserSerializer, GroupSerializer
from .models import SonicRing
from rest_framework import viewsets, permissions

class RingViewSet(viewsets.ModelViewSet):
    """
    automatically provides,  list, 'update', and 'destroy' functions
    """

    queryset = SonicRing.objects.all()
    serializer_class = RingSerializer




# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
