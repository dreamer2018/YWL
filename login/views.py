#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from login.form import ContactForm
from login.models import user, education


# Create your views here.
# 登录页面
def login(request):
    return render_to_response('login.html', {
        'url': '../static/',
    }, context_instance=RequestContext(request))


# 登录信息验证界面
def login_info(request):
    html = ""
    if request.POST:
        phone = request.POST['phone']
        passwd = request.POST['password']
        try:
            u = user.objects.get(phone=phone)
        except user.DoesNotExist:
            html += '<html><body><h2>帐号不存在，请<a href = "/login/ ">重试</a>或去<a href = "/register/">注册</a></h2></body>'
        else:
            if u.passwd == passwd:
                request.session['id'] = u.id
                html += '<html><head><meta http-equiv="refresh" content="3;url=/"><head><body><h2>登录成功，' \
                        '正在跳转.......</h2></body>'
            else:
                html += '<h2>帐号或密码错误，请<a href = "/login/ ">重试</a></h2>'
        return HttpResponse(html)


# 注销
def logout(request):
    del request.session['id']
    return HttpResponseRedirect('/login/')


# 注册页面
def register(request):
    return render_to_response('register.html', {
        'url': '../static/',
        'education': education.objects.all(),
    }, context_instance=RequestContext(request))


# 获取注册信息
def register_info(request):
    html = ''
    if request.POST:
        # 获取数据
        nick_name = request.POST['nick_name']
        real_name = request.POST['real_name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        birthday = request.POST['birthday']
        education = request.POST['education']
        address = request.POST['address']
        introduction = request.POST['introduction']

        # 解析数据正确性
        if len(nick_name) > 20 or len(nick_name) < 2:
            html += '<p>昵称必须大与2小与20</p><br/>'
        if len(real_name) > 20 or len(real_name) < 2:
            html += '<p>姓名必须大与2小与20</p><br/>'
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
        try:
            user.objects.get(phone=phone)
        except user.DoesNotExist:
            pass
        else:
            html += '<p>手机号码已被注册，请换个手机号码重试！<p><br/>'
        if not len(html):
            u = user()
            u.nick_name = nick_name
            u.real_name = real_name
            u.phone = phone
            u.email = email
            u.education = education
            u.passwd = password
            u.birthday = birthday
            u.address = address
            u.about = introduction
            u.save()
    else:
        html = '<html><head><meta http-equiv="refresh" content="3;url=/register/"><head><body><h2>Null</h2></body>'
    if not len(html):
        html = '<html><head><meta http-equiv="refresh" content="3;url=/login/"><head><body><h2>注成功，正在跳转.......' \
               '</h2></body>'
    return HttpResponse(html)

    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         u = user()
    #         u.nick_name = cd['nick_name']
    #         u.real_name = cd['real_name']
    #         u.phone = cd['phone']
    #         u.email = cd['email']
    #         u.education = cd['education']
    #         u.passwd = cd['password']
    #         u.birthday = cd['birthday']
    #         u.address = cd['address']
    #         u.about = cd['introduction']
    #         u.save()
    #         return '<html><head><meta http-equiv="refresh" content="3;url=/register/"><head><body><h2>Null</h2></body>'
    #     else:
    #         form = ContactForm()
    #         return render_to_response('register.html', {'form': form})


def develop(request, offset):
    return render_to_response('develop.html')
