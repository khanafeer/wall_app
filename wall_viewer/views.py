# -*- coding: utf-8 -*-
from django.utils.decorators import method_decorator
from django.shortcuts import redirect,render
from django.views import View
from wall_viewer.forms import UserForm
from django.contrib.auth import login,logout,authenticate
from wall_api.models import Message
def home(request):
    m = Message.objects.all().order_by('-created')
    return render(request,'wall_viewer/wall.html',context={'messages':m})

def register(request):
    return render(request,'wall_viewer/register.html')

def logout_view(request):
    logout(request)
    return redirect('/')

class LoginView(View):
    error_msg = "Something went wrong try login again."
    def get(self,request):
        return render(self.request, 'wall_viewer/login.html')

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                self.error_msg = "Username or Password incorrect."
        return render(self.request, 'wall_viewer/login.html',context={'error':self.error_msg})