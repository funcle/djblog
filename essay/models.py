import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Type(models.Model):

    db_table = "essay_type"

    id = models.AutoField(primary_key=True)
    rank = models.IntegerField(default=0)
    name = models.CharField(max_length=20)
    interfacename = models.CharField(max_length=10)

    @property
    def essay_nums(self):
        objs = Essay.objects.filter(type_id=self.id, display=True)
        return len(objs)


class Essay(models.Model):

    db_table = 'essay_essay'
    
    id = models.AutoField(primary_key=True)
    type_id = models.IntegerField(default=1)
    title = models.CharField(max_length=50, default='')
    content = models.CharField(max_length=100000, default='')
    ctime = models.DateTimeField(default=datetime.datetime.now())
    poster = models.CharField(max_length=20, default='funcle')
    is_reprinted = models.BooleanField(default=False)
    reprinted_url = models.CharField(max_length=200, default='')
    display = models.BooleanField(default=False)

    @property
    def ptype(self):
        return Type.objects.get(pk=self.type_id)

    @property
    def comment_num(self):
        objs = Comment.objects.filter(essay_id=self.id).all()
        return len(objs)


class Comment(models.Model):

    db_table = 'essay_comment'

    id = models.AutoField(primary_key=True)
    essay_id = models.IntegerField(default=1)
    username = models.CharField(max_length=20)
    comment = models.CharField(max_length=500)
    ctime = models.DateTimeField(default=datetime.datetime.now())
    req_ip = models.CharField(max_length=20, default='')
    up_num = models.IntegerField(default=0)
    low_num = models.IntegerField(default=0)
