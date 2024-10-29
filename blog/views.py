from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView,UpdateView
from django.views.generic.dates import ArchiveIndexView, TodayArchiveView

from .forms import BoardForm
from blog.models import Board
# Create your views here.

class BoardEdit(UpdateView):
    model = Board
    form_class = BoardForm
    template_name = 'blog/board_edit.html'

    def form_valid(self, form):    
        return super().form_valid(form)
    def get_success_url(self):
        return super().get_success_url()
    
    

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

