from rest_framework import serializers
from .models import Destination
from django.contrib.auth.models import User

class DestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Destination
        fields = ('name', 'img','desc','price','offer')


# Rest API for Registration
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user 



