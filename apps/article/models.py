# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField

from datetime import datetime


# Create your models here.

class Article(models.Model):
    menu_name = models.CharField(max_length=50, verbose_name=u"菜单名")
    dir_name = models.CharField(max_length=50, verbose_name=u"目录名")
    detail = UEditorField(verbose_name=u"文章详情", width=600, height=300, imagePath="courses/ueditor/",
                          filePath="courses/ueditor/", default='')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面图", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    category = models.CharField(default=u"博客", max_length=20, verbose_name=u"文章类别")
    tag = models.CharField(default="", verbose_name=u"文章标签", max_length=10)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")


class Meta:
    verbose_name = u"文章"
    verbose_name_plural = verbose_name
