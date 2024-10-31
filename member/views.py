from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from .forms import UserSignupForm

# Create your views here.

def Signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            id = form.cleaned_data.get('username')
            pw = form.cleaned_data.get('password1')
            user = authenticate(username=id,password=pw)
            login(request,user)
            return redirect('board:board_list')
        else:
            for fields, errors in form.errors.items():
                label = form.fields[fields].label
                for error in errors:
                    messages.error(request, f"{label}: {error}")
    else:
        form = UserSignupForm()
    return render(request,'member/signup.html',{'form':form})
