from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','email']

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = '아이디'  # username 필드의 레이블을 '아이디'로 변경
        self.fields['password1'].label = '비밀번호'  # password1 필드 레이블 변경
        self.fields['password2'].label = '비밀번호 확인'  # password2 필드 레이블 변경