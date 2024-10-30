from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView,UpdateView,DeleteView
from django.views.generic.dates import ArchiveIndexView, TodayArchiveView

from .forms import BoardForm
from blog.models import Board
# Create your views here.

class BoardDel(DeleteView):
    def post(self,request,pk):
        board = get_object_or_404(Board,pk=pk)
        board.soft_del()
        return redirect('blog:index')

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
    def get_queryset(self):
        return Board.objects.filter(enable=False)
    

class BoardDV(DetailView):
    model = Board

    def get(self, request, *args, **kwargs):
        board = self.get_object()
        board.hits +=1
        board.save()
        return super().get(request, *args, **kwargs)


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

