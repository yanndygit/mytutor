# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View
from .models import Article,Menu,Dir,SubDir,DirRelation,SubDirRelation

# Create your views here.
class DirView(View):

    def get(self, request,article_id=1,menu_id=1):
        all_subDir={}
        all_article = Article.objects.get(id=article_id)
        all_menu = Menu.objects.all()
        all_dir = Dir.objects.filter(menu_id=menu_id)
        for dir in all_dir:
            all_subDir[dir] = SubDir.objects.filter(menu_id=menu_id,dir_id=dir.id)

        dir_relation = DirRelation.objects.all()
        subDir_relation = SubDirRelation.objects.all()

        return render(request, "wiki.html",{
            "article":all_article,
            "all_menu":all_menu,
            "all_dir":all_dir,
            "all_subDir":all_subDir
        })
        #course = Course.objects.get(id=int(course_id))
        #all_resources = CourseResource.objects.filter(course=course)
        #all_comments = CourseComments.objects.all().order_by("-id")
        #return render(request, "course-comment.html", {
        #    "course":course,
        #    "course_resources":all_resources,
        #    "all_comments":all_comments
        #})
