# -*- coding: utf-8 -*-
from django.utils.decorators import method_decorator
from django.shortcuts import redirect,render
from django.views import View
from wall_viewer.forms import UserForm
from django.contrib.auth import login,logout,authenticate
from wall_api.models import Message
def home(request):
    m = Message.objects.all()
    return render(request,'wall_viewer/wall.html',context={'messages':m})

def register(request):
    return render(request,'wall_viewer/register.html')

def logout_view(request):
    logout(request)
    return redirect('/')

class LoginView(View):

    def get(self,request):
        return render(self.request, 'wall_viewer/login.html')

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(self.request, 'wall_viewer/login.html')

# class Question(View):
#     def get(self,request):
#         return render(request,'main_app/question_ask.html')
#
#     @method_decorator(login_required(login_url='/auth/login/'))
#     def post(self,request):
#         pass
# def log_out(request):
#     logout(request)
#     return redirect('/')
#
# class Login(View):
#     def get(self, request):
#         context = {'log_type':'login'}
#         return render(request, 'main_app/login.html',context)
#
#     def post(self, request):
#         data = request.POST
#         if data:
#             uname = data['username']
#             passw = data['password']
#             next = request.GET.get('next', '/')
#             user = authenticate(username=uname,password=passw)
#             if user is not None:
#                 login(request,user)
#                 print next
#                 return redirect(next)
#         messages.error(request, 'Username or password Incorrect')
#         return redirect('/auth/login/')
#
#
# class Signup(View):
#     def get(self, request):
#         form = Sign_up()
#         context = {'log_type': 'signup','form':form}
#         print context
#         return render(request, 'main_app/login.html',context)
#
#     def post(self, request):
#         form = Sign_up(request.POST)
#         if form.is_valid():
#             user = form.save(commit=True)
#             uname = form.cleaned_data.get('username')
#             passw = form.cleaned_data.get('password')
#             login(request,user)
#             print user
#             return redirect('/')
#         messages.error(request, 'Review your inputs')
#         return redirect('/auth/register/')