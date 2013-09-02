from rest_framework import serializers

from people.serializers import PersonSerializer

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'first_name', 'last_name', 'person',)