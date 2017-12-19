# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View
from .models import Article,Menu,Dir,SubDir,DirRelation,SubDirRelation

# Create your views here.
class DirView(View):

    def get(self, request):
        all_article = Article.objects.get(id=3)
        all_menu = Menu.objects.all()
        all_dir = Dir.objects.filter(menu_id=5)
        all_subDir = SubDir.objects.filter(menu_id=1,dir_id=2)
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
