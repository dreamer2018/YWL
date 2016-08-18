#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.db import models


# Create your models here.
# 新闻类型
class news_type(models.Model):
    name = models.CharField(max_length=20)  # 新闻类型名

    def __unicode__(self):
        return u'%s' % self.name


# 活动类型
class activity_type(models.Model):
    name = models.CharField(max_length=20)  # 活动类型名

    def __unicode__(self):
        return u'%s' % self.name


# 捐助类型
class donate_type(models.Model):
    name = models.CharField(max_length=20)  # 捐助类型名

    def __unicode__(self):
        return u'%s' % self.name


# 公益招募职位类型
class jobs_type(models.Model):
    name = models.CharField(max_length=20)  # 公益招募职位名

    def __unicode__(self):
        return u'%s' % self.name


# 新闻动态
class news(models.Model):
    type = models.ForeignKey(news_type)  # 新闻类型
    title = models.CharField(max_length=40)  # 新闻标题
    author = models.CharField(max_length=20)  # 作者，编辑
    time = models.DateTimeField(auto_now_add=True)  # 发布时间
    url = models.URLField()  # 来源
    read = models.IntegerField()  # 阅读量
    text = models.TextField()  # 主要内容

    def __unicode__(self):
        return u'%s' % self.title


# 专题活动
class activity(models.Model):
    type = models.ForeignKey(activity_type)  # 活动类型，线上，线下
    title = models.CharField(max_length=40)  # 活动标题
    sponsor = models.CharField(max_length=40)  # 活动发起方
    start = models.DateTimeField()  # 活动开始时间
    end = models.DateTimeField()  # 活动结束时间
    address = models.CharField(max_length=100)  # 活动地址
    text = models.TextField()  # 活动主要内容

    def __unicode__(self):
        return u'%s' % self.title


# 公益招募
class join(models.Model):
    type = models.ForeignKey(jobs_type)  # 职位名
    address = models.CharField(max_length=20)  # 招募地点
    name = models.CharField(max_length=40)  # 机构名称
    job = models.CharField(max_length=20)  # 招募职位
    number = models.IntegerField()  # 招聘人数
    time = models.DateTimeField()  # 发布时间

    def __unicode__(self):
        return self.id


# 公益捐赠
class donate(models.Model):
    title = models.CharField(max_length=40)  # 捐助标题
    type = models.ForeignKey(donate_type)  # 捐助类型 
    time = models.DateTimeField()  # 捐助日期
    text = models.TextField()  # 捐助内容

    def __unicode__(self):
        return u'%s' % self.title


# 图片
class picture(models.Model):
    title = models.CharField(max_length=40)
    url = models.ImageField(upload_to='./static/')
    text = models.TextField()

    def __unicode__(self):
        return u'%s' % self.title
