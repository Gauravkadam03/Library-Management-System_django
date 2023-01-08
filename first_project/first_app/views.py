from django.shortcuts import render
from .models import student

# Create your views here.
def index_view(request):
    return render(request,'first_app/index.html')

def addition(request,a,b):
    c=a+b
    d=a-b
    e=a*b
    try:
        f=a//b
    except :
        f='error'
    context={
        'a':a,
        'b':b,
        'c':c,
        'd':d,
        'e':e,
        'f':f
    }
    return render(request,'first_app/addition.html',context)

def info(request):
    n='Gaurav kadam'
    c='BCA'
    s='Python,Django'
    context={
        'name':n,
        'class':c ,
        'skill':s   }
    return render(request,'first_app/info.html',context)

def table(request):
    db=[
        {'name':'Mohit','sal':23400,'dep':'Full stack','id':101},
        {'name':'Gaurav','sal':22500,'dep':'Backend','id':102},
        {'name':'Ankit','sal':45400,'dep':'Frontend','id':103},
        {'name':'Ajay','sal':78900,'dep':'Hr','id':104},
        {'name':'Viru','sal':32400,'dep':'Gaming','id':105},
        {'name':'Vijay','sal':37800,'dep':'Full stack','id':106},
        {'name':'Moti','sal':78900,'dep':'Testing','id':107},
        {'name':'Jay','sal':12300,'dep':'Hr','id':108},
    ]
    context={
        'data':db
    }
    return render(request,'first_app/table.html',context)

def orm(request):
    data=student.objects.all()
    context={
        'data':data
    }
    return render(request,'first_app/orm.html',context)

def frm(request):
    if request.method=='POST':
        # print(request.POST)
        n=request.POST.get('name')
        r=request.POST.get('roll')
        m=request.POST.get('mrk')
        print(n,r,m)
    return render (request,"first_app/form.html")

def a(request):
    if request.method=='POST' :
        # print(request.POST)
        n=request.POST.get('name')
        context={
            'name':n
        }
    return render (request,'first_app/welcome.html',context)