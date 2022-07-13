from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import SonicRing


class RingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SonicRing
        fields =[ 'created', 'material', 'shape']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']