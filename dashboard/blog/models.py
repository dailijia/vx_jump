from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
    titie = models.CharField("标题",max_length=50,null=True)
    writer = models.CharField("作者",max_length=50)
    created_date = models.DateFiled("创建时间",auto_now_add=True)
    mofify_date = models.DateFiled("修改时间",auto_now=True)
    content = models.TextFiled()
    is_show = models.BooleanFiled()

    class Meta；
        db_table = "artile"

    def __str__(self):
    	return self.title