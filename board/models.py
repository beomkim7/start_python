from django.db import models
from django.utils import timezone
from django.urls import reverse

class BoardQuerySet(models.QuerySet):
    def active(self):
        return self.filter(enable=False)


# Create your models here.
class Board(models.Model):
    # author = models.ForeignKey('auth.User',on_delete=models.CASCADE)

    title = models.CharField(verbose_name='TITLE',max_length=100)
    content = models.TextField('CONTENT',default='')
    hits = models.PositiveIntegerField('HITS',default=0)
    pub_date = models.DateTimeField('PUBLISH DATE',default = timezone.now)
    mod_date = models.DateTimeField('MODIFY DATE',auto_now = True)
    enable = models.BooleanField(default=False)

    class Meta:
        verbose_name='Board'
        verbose_name_plural='Boards'
        db_table='board_Boards'
        ordering=('-id',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('board:board_detail',args=(self.id,))
    
    def get_previous(self):
        return Board.objects.filter(id__lt=self.id,enable=False).order_by('pk').last()

    def get_next(self):
        return Board.objects.filter(id__gt=self.id,enable=False).order_by('pk').first()

    def soft_del(self):
        self.enable = True
        self.save()

    objects = BoardQuerySet.as_manager()
    