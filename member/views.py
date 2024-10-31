from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import UserSignupForm, UserSigninForm

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
        form = UserSigninForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "로그인 성공!")
                return redirect('board:board_list')
            else:
                messages.error(request, "아이디 또는 비밀번호를 확인하세요.")
        else:
            # 폼 유효성 검사에서 오류가 발생한 경우
            print(form.errors)  # 오류를 출력
            messages.error(request, "아이디 또는 비밀번호를 확인하세요1.")
            return redirect('member:signin')
    else:
        form = UserSigninForm()

    return render(request, 'member/signin.html', {'form': form})
