from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('',views.BoardLV.as_view(),name = 'index'),
    path('board/',views.BoardLV.as_view(),name='board_list'),
    path('board/<int:pk>/',views.BoardDV.as_view(),name='board_detail'),
    path('achive/',views.BoardAV.as_view(),name='board_archive'),
    path('achive/<int:year>/',views.BoardYAV.as_view(),name='board_year_archive'),
    path('achive//<int:year>/<int:month>/',views.BoardMAV.as_view(),name='board_month_archive'),
    path('achive/<int:year>/<int:month>/',views.BoardDAV.as_view(),name='board_day_archive'),
    path('achive/<int:year>/<int:month>/<int:day>/',views.BoardDAV.as_view(),name='board_day_archive'),
    path('achive/today',views.BoardTAV.as_view(),name='board_today')
]