#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
    Create By zhoupan At 2016.08.17
"""

from django.db import models


# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=20)  # 用户名
    phone = models.CharField(max_length=11, unique=True)  # 手机号码
    passwd = models.CharField(max_length=20)  # 密码
    birthday = models.CharField(max_length=10, blank=True)  # 生日
    address = models.CharField(max_length=40, blank=True)  # 地址
    about = models.TextField()  # 个人说明

    def __unicode__(self):
        return u' %s ' % self.name