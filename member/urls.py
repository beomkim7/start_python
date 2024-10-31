from django.urls import path
from . import views

app_name = 'member'

urlpatterns = [
    path('signup/',views.Signup,name='signup'),
    path('signout/',views.Signout,name='signout'),
    path('signin/',views.Signin,name='signin'),
]
