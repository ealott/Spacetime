from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Event, Tool

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = [ 'name','short_description', 'event_start',]

class ToolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'