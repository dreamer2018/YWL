#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""YWL URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from ywl_site.views import *

# 系统
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),  # 首页
]

# APP ： ywl_site
urlpatterns += [
    url(r'^test/(\d)/$', test),  # 测试
    url(r'^news/$', newss), url(r'^news/(\d)/$', news_view),  # 新闻动态
    url(r'^activity/$', activitys), url(r'^activity/(\d)/$', activity_view),  # 专题活动
    url(r'^join/$', joins), url(r'^join/(\d)/$', join_view),  # 公益招募
    url(r'^donate/$', donates), url(r'^donate/(\d)/$', donate_view),  # 乐捐
    url(r'^about/$', about),  # 关于我们
    url(r'^contact/$', contact),  # 联系我们
    url(r'^picture/(\d)/$', pictures),  # 图说动态
]

# APP： login
urlpatterns += [
    url(r'^login/$', 'login.views.login'),  # 登录
    url(r'^register/$', 'login.views.register'),  # 注册
    url(r'^register_info/$', 'login.views.register_info'),  # 注册信息
    url(r'^login_info/$', 'login.views.login_info'),  # 登录信息
    url(r'^logout/$', 'login.views.logout'),  # 注销
    url(r'^user/(\d)/$', 'login.views.develop'),
]
