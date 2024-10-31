from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
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
            for field, errors in form.errors.items():
                label = form.fields[field].label
                for error in errors:
                    messages.error(request, f"{label}: {error}")
    else:
        form = UserSignupForm()
    return render(request,'member/signup.html',{'form':form})

def Signout(request):
    logout(request)
    messages.success(request,'로그아웃')
    return redirect('board:board_list')

def Signin(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        print(request)
        if form.is_valid():
            id = form.cleaned_data.get('username')
            pw = form.cleaned_data.get('password')
            user = authenticate(username=id,password=pw)
            if user is not None:
                login(request,user)
                messages(request,"로그인 성공!")
                return redirect('board:board_list')
            else:
                messages(request,"아이디,비번확인")
    else:
        form = UserSignupForm()
    return render(request,'member/signin',{'form':form})