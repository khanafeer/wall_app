from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect,render
from django.contrib.auth import login
from wall_api.permissions import IsOwnerOrReadOnly
from wall_api.serializers import MessageSerializer,UserSerializer
from wall_api.models import Message



class MessageView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def post(self,request):
        newdict = {'user': self.request.user.id,'content':self.request.data['content']}
        ser = MessageSerializer(data=newdict)
        if ser.is_valid():
            ser.save()
        return redirect('/',self.request)

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        try:
            print(request.data)
            serialized = UserSerializer(data=request.data)
            if serialized.is_valid():
                User.objects.create_user(
                    serialized.validated_data['username'],
                    serialized.validated_data['email'],
                    serialized.validated_data['password']
                )
                #send_mail('welcome message','welcome to Wall App','naser_khanafeer@yahoo.com',[serialized.validated_data['email']])
                login(request,User.objects.get(username=serialized.validated_data['username']))
                return redirect('/',request)
            else:
                return render(request, 'wall_viewer/register.html',
                              context={'error': serialized.errors}
                              )
                #return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return render(request, 'wall_viewer/register.html',
                          context={'error': 'Something went wrong try Register again.'}
                          )
            #return Response(ex,status.HTTP_400_BAD_REQUEST)
