# blog/forms.py

from django import forms
from .models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title','content']  # 제목 필드를 자동 완성으로 설정
        widgets = {
              'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '제목을 입력하세요'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '내용을 입력하세요', 'rows': 5}),
        }
        
