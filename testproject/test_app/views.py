from django.shortcuts import render,redirect,HttpResponse
from .models import student
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth

# Create your views here.
def signup(request):
    # fm=signupform(request)
    # if request.method == 'POST':
    #     if fm.is_valid():
    #         fm.save()
    #         return redirect('/signin/')
            
    #     else:
    #         pass
    
    # return render(request,'test_app/signup.html',{'form' : fm})
    if request.method == 'POST':
        n=request.POST.get('username')
        e=request.POST.get('email')
        p=request.POST.get('password')
        p1=request.POST.get('password1')
        if p==p1:
            if User.objects.filter(username=n).exists():
                messages.error(request,'username taken')
                return redirect ('/signup/')
            elif User.objects.filter(email=e).exists():
                messages.error(request,'email taken')
                return redirect ('/signup/')
            else:
                user=User.objects.create_user(username=n,email=e,password=p)
                user.save()
                return redirect ('/signin/')
        else:
            messages.error(request,'password not matched')
            

    return render(request,'test_app/signup.html')


def img(request):
    return render(request,'test_app/index.html')

def form(request):
    if request.method == 'POST':
        n=request.POST.get('name')
        m=request.POST.get('marks')
        j=student(name=n,marks=m)
        j.save()
        
        
        return redirect('/display/')

    return render(request,'test_app/form.html')

@login_required(login_url="/signin/")
def display(request):
    data=student.objects.all()
    context={'data':data}
    return render(request,'test_app/display.html',context)

# def login(request):
#     if request.method == 'POST':
#         n=request.POST.get('u_name')
#         m=request.POST.get('pass') 
#         user = authenticate(Username=n,Password=m)
#         if user is not None:
#             login(request,user)
#             return HttpResponse('<h1>hello<h1>')
#         else:
#             pass
#     return render(request,'test_app/login.html')

def login1(request):
    if request.user.is_authenticated:
        return redirect('/display')
    else:
        
        # fm=loginform(request.POST)
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/display/')
            else:
                messages.error(request,'invalid credintials')
                return redirect('/signin/')
   
        



    # return render(request,'test_app/login.html',{'form':fm})
    return render(request,'test_app/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/signin/')