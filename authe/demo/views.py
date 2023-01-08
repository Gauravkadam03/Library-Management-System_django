from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import createuserform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('/index/')
    else:
        form=createuserform()
        if request.method =='POST':
            form=createuserform(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'account was created for '+ user)
                return redirect ('/signin/')


        return render(request,'demo/signup.html',{'form':form})

def signin(request):
    if request.user.is_authenticated:
        return redirect('/index/')
    else:
        if request.method =='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/index/')
            # else:
            #     messages.info()

        return render(request,'demo/login.html')

@login_required(login_url='/signin/')
def index1(request):

    return render(request,'demo/index.html')

def logout(request):
    auth.logout(request)
    return redirect('/signin/')