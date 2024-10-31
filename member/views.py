from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from .forms import UserSignupForm

# Create your views here.

def Signup(request):
    if request.method == 'post':
        form = UserSignupForm(request.post)        
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('Singup')
    else:
        form = UserSignupForm()
        return render(request,'member/signup.html',{'form':form})
