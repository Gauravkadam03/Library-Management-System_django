from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import createuserform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth

# Create your views here.
@login_required(login_url='/signin/')
def index(request):
    return render(request,'library_app/index.html')

@login_required(login_url='/signin/')
def form(request):
    if request.method=='POST':
        nm=request.POST.get('bname')
        an=request.POST.get('aname')
        dt=request.POST.get('date')
        cat=request.POST.get('category')
        
        a=book(B_name=nm,A_name=an,Date=dt,B_category=cat)
        a.save()
        return redirect('/display/')


    return render(request,'library_app/form.html')

# def display(request):
#     data=book.objects.all()
#     context={
#         'data':data
#     }
#     return render(request,'library_app/display.html',context)

@login_required(login_url='/signin/')
def display(request):
    data=book.objects.all()
    context={
        'data':data
    }
    if request.method=='POST':
        val=request.POST.get('val')
        data=book.objects.filter(B_name__contains=val)
        context1={
        'data':data
    }
        return render(request,'library_app/search_display.html',context1)
        
        
    
    return render(request,'library_app/display.html',context)

@login_required(login_url='/signin/')
def display_update(request):
    data=book.objects.all()
    context={
        'data':data
    }
    return render(request,'library_app/display_update.html',context)

@login_required(login_url='/signin/')
def update(request,j):
    data=book.objects.get(id=j)
    context={
        'data':data
    }
    if request.method=='POST':
        nm=request.POST.get('bname')
        an=request.POST.get('aname')
        dt=request.POST.get('date')
        cat=request.POST.get('category')
        
        data.B_name=nm
        data.A_name=an
        data.Date=dt
        data.B_category=cat
        data.save()
        return redirect('/display/')

    return render(request,'library_app/update.html',context)

@login_required(login_url='/signin/')
def delete(request,j):
    data=book.objects.get(id=j)
    context={
        'data':data
    }
    if request.method=='POST':
        data.delete()
        return redirect('/display/')


    return render(request,'library_app/delete.html',context)

@login_required(login_url='/signin/')    
def display_delete(request):
    data=book.objects.all()
    context={
        'data':data
    }
    return render(request,'library_app/display_delete.html',context)
     
# def login11(request):
#     return render(request,'library_app/a_login.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/index/')
    else:
        # form=createuserform()
        # if request.method =='POST':
        #     form=createuserform(request.POST)
        #     if form.is_valid():
        #         form.save()
        #         user=form.cleaned_data.get('username')
        #         messages.success(request,'account was created for '+ user)
        #         return redirect ('/signin/')
          
          if request.method =='POST':
            username=request.POST.get('username')
            email=request.POST.get('password')
            password=request.POST.get('username')
            password1=request.POST.get('password')
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect ('/signin/')


    return render(request,'library_app/signup.html',{'form':form})

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
            else:
                messages.info(request,'invalid credentials')
    return render(request,'library_app/a_login.html')

def logout(request):
    auth.logout(request)
    return redirect('/signin/')