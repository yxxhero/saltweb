#coding:utf-8
from django.contrib import admin
from saltweb import models
# Register your models here.
class articleinfo(admin.ModelAdmin):
    list_display=('title','title_link','user_home','author','createtime','classify','is_stick','is_fine','answer','views','head_sculpture')
    raw_id_fields = ("author",)
class usertype(admin.ModelAdmin):
    list_display=('id','username','password')
class chatinfo(admin.ModelAdmin):
    list_display=('id','username','createtime','chatcontent')
    raw_id_fields = ("username",)
class commentinfo(admin.ModelAdmin):
    list_display=('id','username','articlename','createtime','content')
    raw_id_fields = ("username","articlename")
admin.site.register(models.userinfo,usertype)
admin.site.register(models.saltcommandhistory)
admin.site.register(models.article,articleinfo)
admin.site.register(models.comment,commentinfo)
admin.site.register(models.chatmodel,chatinfo)
