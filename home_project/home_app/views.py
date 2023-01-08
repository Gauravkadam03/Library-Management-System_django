from django.shortcuts import render
from .models import student

# Create your views here.
def home(request):
    data=student.objects.all()
    context={
        'data':data
    }
    return render(request,'home_app/index.html',context)