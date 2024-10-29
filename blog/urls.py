from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('',views.BoardLV.as_view(),name = 'index'),
    path('board/',views.BoardLV.as_view(),name='board_list'),
    path('board/<int:pk>/',views.BoardDV.as_view(),name='board_detail'),
    path('board/<int:pk>/edit/',views.BoardEdit.as_view(),name='board_edit'),
]