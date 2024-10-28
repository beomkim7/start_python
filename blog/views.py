from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, TodayArchiveView

from blog.models import Board
# Create your views here.


class BoardLV(ListView):
    model = Board
    context_object_name = 'boards'
    paginate_by =2

class BoardDV(DetailView):
    model = Board

class BoardAV(ArchiveIndexView):
    model = Board
    date_field = 'mod_date'

class BoardYAV(ArchiveIndexView):
    model = Board
    date_field = 'mod_date'
    make_object_list = True

class BoardMAV(ArchiveIndexView):
    model = Board
    date_field = 'mod_date'

class BoardDAV(ArchiveIndexView):
    model = Board
    date_field = 'mod_date'

class BoardTAV(TodayArchiveView):
    model = Board
    date_field = 'mod_date'

