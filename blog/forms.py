# blog/forms.py

from django import forms
from dal import autocomplete
from .models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title']  # 제목 필드를 자동 완성으로 설정
        widgets = {
            'title': autocomplete.ModelSelect2(url='board-autocomplete'),  # URL은 나중에 정의
        }
