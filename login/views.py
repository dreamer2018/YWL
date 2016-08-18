#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.shortcuts import render_to_response


# Create your views here.
# 登录页面
def login(request):
    return render_to_response('login.html', {
        'url': '../static/',
    }
                              )


# 注册页面
def register(request):
    return render_to_response('register.html', {
        'url': '../static/'
    }
                              )
