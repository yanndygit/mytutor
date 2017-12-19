# _*_ coding:utf-8 _*_
import xadmin

from .models import Article,Dir,Menu,SubDir,DirRelation,SubDirRelation


class ArticleAdmin(object):
    list_display = ['detail', 'students']
    search_fields = ['detail', 'students']
    list_filter = ['detail', 'students']

    style_fields = {"detail":"ueditor"}

class DirAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name','menu']

class SubDirAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name','dir']

class MenuAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class DirRelationAdmin(object):
    list_display = ['current_dir']
    search_fields = ['current_dir']
    list_filter = ['current_dir']



class SubDirRelationdmin(object):
    list_display = ['current_subDir']
    search_fields = ['current_subDir']
    list_filter = ['current_subDir']

xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Menu,MenuAdmin)
xadmin.site.register(Dir,DirAdmin)
xadmin.site.register(SubDir,SubDirAdmin)
xadmin.site.register(DirRelation,DirRelationAdmin)
xadmin.site.register(SubDirRelation,SubDirRelationdmin)


