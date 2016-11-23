#coding:utf-8
from django.db import models

# Create your models here.
class userinfo(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=255)
    updatetime=models.DateTimeField(auto_now = True)
    createtime=models.DateTimeField(auto_now_add = True)
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
    def __unicode__(self):
        return self.username
class saltcommandhistory(models.Model):
    username=models.CharField(max_length=30)
    createtime=models.DateTimeField(auto_now_add = True)
    minions=models.CharField(max_length=255)
    miniontype=models.CharField(max_length=255)
    module=models.CharField(max_length=255)
    arg=models.CharField(max_length=255,null=True)
    class Meta:
        verbose_name = '命令历史'
        verbose_name_plural = '命令历史'
class article(models.Model):
    title=models.CharField(max_length=255)
    title_link=models.CharField(max_length=255)
    author=models.ForeignKey(userinfo)
    user_home=models.CharField(max_length=255)
    createtime=models.DateTimeField(auto_now_add = True)
    classify=models.CharField(max_length=255)
    is_stick=models.BooleanField()
    is_fine=models.BooleanField()
    answer=models.PositiveSmallIntegerField()
    views=models.PositiveSmallIntegerField()
    head_sculpture=models.CharField(max_length=255)
    class Meta:
        verbose_name = '文章信息'
        verbose_name_plural = '文章信息'
    def __unicode__(self):
        return self.title
class comment(models.Model):
    username=models.ForeignKey(userinfo)
    articlename=models.ForeignKey(article)
    createtime=models.DateTimeField(auto_now_add = True)
    content=models.CharField(max_length=255)
    class Meta:
        verbose_name = '评论信息'
        verbose_name_plural = '评论信息'
class chatmodel(models.Model):
    username=models.ForeignKey(userinfo)
    createtime=models.DateTimeField(auto_now_add = True)
    chatcontent=models.CharField(max_length=255)
    class Meta:
        verbose_name = '聊天记录'
        verbose_name_plural = '聊天记录'
