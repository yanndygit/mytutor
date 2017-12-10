# _*_ coding:utf-8 _*_
import xadmin

from .models import Article,Dir,Menu


class ArticleAdmin(object):
    list_display = ['detail', 'students']
    search_fields = ['detail', 'students']
    list_filter = ['detail', 'students']

    style_fields = {"detail":"ueditor"}

class DirAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class MenuAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Menu,MenuAdmin)
xadmin.site.register(Dir,DirAdmin)

