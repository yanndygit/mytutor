# _*_ coding:utf-8 _*_
import xadmin

from .models import Article


class ArticleAdmin(object):
    list_display = ['menu_name', 'dir_name', 'detail', 'students']
    search_fields = ['dir_name', 'detail', 'detail', 'students']
    list_filter = ['dir_name', 'detail', 'detail', 'students']

xadmin.site.register(Article,ArticleAdmin)
