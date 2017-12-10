# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View
from .models import Article

# Create your views here.
class DirView(View):
    def get(self, request):
        all_article = Article.objects.get(id=1)
        return render(request, "article.html",{
            "article":all_article
        })
        #course = Course.objects.get(id=int(course_id))
        #all_resources = CourseResource.objects.filter(course=course)
        #all_comments = CourseComments.objects.all().order_by("-id")
        #return render(request, "course-comment.html", {
        #    "course":course,
        #    "course_resources":all_resources,
        #    "all_comments":all_comments
        #})
