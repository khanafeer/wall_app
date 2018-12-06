from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.core.mail import send_mail

from wall_api.permissions import IsOwnerOrReadOnly
from wall_api.serializers import MessageSerializer,UserSerializer
from wall_api.models import Message


class MessageViewSet(ModelViewSet):
    """
        A viewset for viewing and editing Message instances.
    """
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        try:
            serialized = UserSerializer(data=request.data)
            if serialized.is_valid():
                User.objects.create_user(
                    serialized.validated_data['username'],
                    serialized.validated_data['email'],
                    serialized.validated_data['password']
                )
                #send_mail('welcome message','welcome to Wall App','naser.khanafeer@gmail.com',[serialized.validated_data['email']])
                return Response(serialized.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(ex,status.HTTP_400_BAD_REQUEST)




