#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
    Create By zhoupan At 2016.08.17
"""

from django.db import models


# Create your models here.
class education(models.Model):
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return u'%s' % self.name


class user(models.Model):
    nick_name = models.CharField(max_length=20)  # 昵称
    real_name = models.CharField(max_length=20)  # 真名
    phone = models.CharField(max_length=11, unique=True)  # 手机号码
    email = models.EmailField()  # 常用邮箱
    passwd = models.CharField(max_length=20)  # 密码
    birthday = models.CharField(max_length=10, blank=True)  # 生日
    address = models.CharField(max_length=40, blank=True)  # 常住地址
    education = models.IntegerField()  # 学历
    about = models.TextField(blank=True)  # 个人说明
    def __unicode__(self):
        return u' %s ' % self.nick_name
