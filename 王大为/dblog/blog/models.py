# -*- coding: UTF-8 -*-
from django.db import models
            
class Tag(models.Model):
    tag_name = models.CharField(u'名称',max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    class Meta:
       #db_table = 'Article' #数据库名
       verbose_name='标签' #修改从管理级进入后的页面显示，显示为'标签'
       verbose_name_plural='标签'#修改管理级页面显示
            
    def __unicode__(self):
        return self.tag_name
            
class Classification(models.Model):
    name = models.CharField(u'名称',max_length=20)
    class Meta:
       #db_table = 'Article' #数据库名
       verbose_name='分类' #修改从管理级进入后的页面显示，显示为'分类'
       verbose_name_plural='分类'#修改管理级页面显示
            
    def __unicode__(self):
        return self.name
            
class Author(models.Model):
    name = models.CharField(u'作者名',max_length=30)
    email = models.EmailField(blank=True,verbose_name='e-mail')
    website = models.URLField(blank=True,verbose_name=u'个人地址')
    class Meta:
       #db_table = 'Article' #数据库名
       verbose_name='作者' #修改从管理级进入后的页面显示，显示为'作者'
       verbose_name_plural='作者'#修改管理级页面显示
            
    def __unicode__(self):
        return u'%s' % (self.name)
            
class Article(models.Model):
    caption = models.CharField(u'标题',max_length=30)
    subcaption = models.CharField(u'副标题',max_length=50, blank=True)
    publish_time = models.DateTimeField(auto_now_add=True,verbose_name=u'发表时间')
    update_time = models.DateTimeField(auto_now=True,verbose_name=u'更新时间')
    author = models.ForeignKey(Author,verbose_name=u'作者')
    classification = models.ForeignKey(Classification,verbose_name=u'分类')
    tags = models.ManyToManyField(Tag, blank=True,verbose_name=u'标签')
    content = models.TextField(verbose_name=u'内容')
    class Meta:
       #db_table = 'Article' #数据库名
       verbose_name='文章' #修改从管理级进入后的页面显示，显示为'文章'
       verbose_name_plural='文章'#修改管理级页面显示


class Users(models.Model):  
    #相当于varchar字符类型  
    uname=models.CharField(verbose_name='用户名',max_length=25)  
    pwd=models.CharField(verbose_name='密码',max_length=12)  
    sex=models.CharField(verbose_name='性别',choices=(("M","男"),("F","女")),max_length=1)  
    email=models.CharField(max_length=25)     
    last_login_ip=models.IPAddressField(verbose_name='最后登录IP')  
    last_login_date=models.DateTimeField(verbose_name='最后登录日期')  
    #重载meta模块,修改Admin后台中显示的名称  
    class Meta:  
        verbose_name = '用户'  
        verbose_name_plural = '用户列表'  
    def __unicode__(self):  
        return self.uname  
    