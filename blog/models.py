from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Board(models.Model):
    # author = models.ForeignKey('auth.User',on_delete=models.CASCADE)

    title = models.CharField(verbose_name='TITLE',max_length=100)
    content = models.TextField('CONTENT',default='')
    pub_date = models.DateTimeField('PUBLISH DATE',default = timezone.now)
    mod_date = models.DateTimeField('MODIFY DATE',auto_now = True)

    class Meta:
        verbose_name='Board'
        verbose_name_plural='Boards'
        db_table='blog_Boards'
        ordering=('-mod_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:board_detail',args=(self.id,))
    
    def get_privious(self):
        return self.get_previous_by_mod_date()
    
    def get_next(self):
        return self.get_next_by_mod_date()