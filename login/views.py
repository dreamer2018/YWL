#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from login.models import user


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
    }, context_instance=RequestContext(request))


# 获取注册信息
def register_info(request):
    html = ""
    if request.POST:
        # 获取数据
        user_name = request.POST['user_name']
        phone = request.POST['phone']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        birthday = request.POST['birthday']
        address = request.POST['address']
        introduction = request.POST['introduction']

        # 解析数据正确性
        if len(user_name) > 20 or len(user_name) < 2:
            html += '<p>用户名必须大与4小与20</p><br/>'
        if len(phone) != 11:
            html += '<p>手机号码输入错误</p><br/>'
        if password != password_confirm:
            html += '<p>两次输入的密码不一致</p></br/>'
        if len(password) < 6 or len(password) > 20:
            html += '<p>密码长度不合法</p><br/>'
        if len(birthday) != 10:
            html += '<p>日期不合法</p><br/>'
        if len(address) > 40:
            html += '<p>地址过长</p><br/>'


        if not len(html):
            u = user()
            u.name = user_name
            u.phone = phone
            u.passwd = password
            u.birthday = birthday
            u.address = address
            u.about = introduction
            u.save()
    else:
        html = '<html><head><meta http-equiv="refresh" content="5;url=/register/"><head><body><h2>Null</h2></body>'
    if not len(html):
        html = '<html><head><meta http-equiv="refresh" content="5;url=/login/"><head><body><h2>注成功，正在跳转.......' \
               '</h2></body>'
    return HttpResponse(html)
