
from django.contrib import admin
from django.urls import path
from home_app.views import *
# from home_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', home),
]
