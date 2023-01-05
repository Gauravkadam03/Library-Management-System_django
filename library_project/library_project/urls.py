
from django.contrib import admin
from django.urls import path,include
from library_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
     path("accounts/", include("django.contrib.auth.urls")),
    path('index/', index),
    path('form/', form),
    path('display/', display),
    path('display_update/', display_update),
    path('update/<int:j>/', update),
    path('delete/<int:j>/', delete),
    path('display_delete/', display_delete),
    path('signin/', signin),
    path('signup/', signup),
    path('logout/', logout),
    # path('login/', login11),
 
]
