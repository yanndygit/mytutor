# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField

from datetime import datetime



# Create your models here.

class Article(models.Model):
    #menu_name = models.ForeignKey(Menu, verbose_name=u"菜单名", null=True, blank=True)
    #dir_name = models.ForeignKey(Dir, verbose_name=u"目录名", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"文章标题")
    detail = UEditorField(verbose_name=u"文章详情", width=600, height=300, imagePath="article/ueditor/",
                          filePath="article/ueditor/", default='')
    students = models.IntegerField(default=0, verbose_name=u'访问次数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面图", max_length=100,null=True,blank=True)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    category = models.CharField(default=u"博客", max_length=20, verbose_name=u"文章类别")
    tag = models.CharField(default="", verbose_name=u"文章标签", max_length=10)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    modify_time = models.DateTimeField(default=datetime.now, verbose_name=u"更新时间")
    modify_nums = models.IntegerField(default=0, verbose_name=u"更新次数")



    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = verbose_name


    def __unicode__(self):
        return self.name

class  Menu(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"菜单名")

    class Meta:
        verbose_name = u"菜单"
        verbose_name_plural = verbose_name


    def __unicode__(self):
        return self.name


class Dir(models.Model):
    menu =  models.ForeignKey(Menu, verbose_name=u"菜单", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"目录名")
    #next_dirId = models.CharField(max_length=10, verbose_name=u"下一个目录ID")
    #next_dir =  models.ForeignKey(Dir, verbose_name=u"下一个目录", null=True, blank=True)
    is_firstDir =  models.BooleanField(default=False, verbose_name=u"是否是第一个目录")
    article = models.ForeignKey(Article, verbose_name=u"文章", null=True, blank=True)


    class Meta:
        verbose_name = u"目录"
        verbose_name_plural = verbose_name


    def __unicode__(self):
        return self.name


class SubDir(models.Model):
    menu = models.ForeignKey(Menu,verbose_name=u"菜单")
    dir =  models.ForeignKey(Dir, verbose_name=u"一级目录")
    name = models.CharField(max_length=50, verbose_name=u"子目录名")
    #next_subDirId = models.CharField(max_length=10, verbose_name=u"下一个子目录ID")
    is_firstDir =  models.BooleanField(default=False, verbose_name=u"是否是第一个子目录")
    article = models.ForeignKey(Article, verbose_name=u"文章", null=True, blank=True)


    class Meta:
        verbose_name = u"子目录"
        verbose_name_plural = verbose_name


    def __unicode__(self):
        return self.name


class DirRelation(models.Model):
    current_menu = models.ForeignKey(Menu, verbose_name=u"当前菜单")
    current_dir = models.ForeignKey(Dir, verbose_name=u"当前目录")
    pre_dir = models.ForeignKey(Dir, verbose_name=u"前一个目录", null=True,blank=True,related_name='pre_dir')
    next_dir = models.ForeignKey(Dir, verbose_name=u"后一个目录", null=True,blank=True,related_name='next_dir')

    class Meta:
        verbose_name = u"目录关系"
        verbose_name_plural = verbose_name


    #def __unicode__(self):
    #    return self.current_dir


class SubDirRelation(models.Model):
    current_menu = models.ForeignKey(Menu, verbose_name=u"当前菜单")
    current_dir = models.ForeignKey(Dir, verbose_name=u"当前目录")
    current_subDir = models.ForeignKey(SubDir, verbose_name=u"当前子目录", null=True, blank=True)
    pre_subDir = models.ForeignKey(SubDir, verbose_name=u"前一个子目录", null=True,blank=True,related_name='pre_subDir')
    next_subDir = models.ForeignKey(SubDir, verbose_name=u"后一个子目录",null=True,blank=True, related_name='next_subDir')

    class Meta:
        verbose_name = u"子目录关系"
        verbose_name_plural = verbose_name


    #def __unicode__(self):
    #    return self.current_subir
