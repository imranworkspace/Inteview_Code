from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User

def login_user(sender,request,user,**kwargs):
    print('inside login user view')
    print('sender ',sender)
    print('receiver ',request   )
    print('user ',user)
    print(f'kwargs {kwargs}')

user_logged_in.connect(login_user,sender=User)