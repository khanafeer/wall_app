from rest_framework.serializers import ModelSerializer
from wall_api.models import Message
from django.contrib.auth.models import User

class MessageSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username','email','password')