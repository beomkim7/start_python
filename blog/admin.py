from django.contrib import admin
from blog.models import Board

# Register your models here.

# admin.site.register(Board)
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id','title','mod_date','hits')
    list_filter=('mod_date','enable',)
    search_fields=('title','content')
    ordering = ('-mod_date',)