from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

# class loginform(AuthenticationForm):
#     class Meta():
#         model=User
#         fields=['username','password1']

class signupform(AuthenticationForm):
    class Meta():
        model=User
        fields=['username','email','password']
