#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Create your views here.
from django.shortcuts import render_to_response

from login.models import *
from ywl_site.models import *


def index(request):
    render = {
        'current_name': '首页',
        'url': '../static/',
        'donate': donate.objects.all(),
        'news': news.objects.all(),
        'activity': activity.objects.all(),
        'join': join.objects.all(),
        'about': picture.objects.all()[0:4],
        'picture': picture.objects.all(),
    }
    if request.session.has_key('id'):
        render['user'] = user.objects.get(id=request.session['id'])
    return render_to_response('index.html', render)


def newss(request):
    render = {
        'current_name': '新闻动态',
        'url': '../static/',
        'news': news.objects.all(),
        'new': news.objects.all()[0:5],
        'hot': news.objects.order_by('read')[0:5]
    }
    if request.session.has_key('id'):
        render['user'] = user.objects.get(id=request.session['id'])
    return render_to_response('news.html', render)


def news_view(request, offset):
    render = {
        'url': '../../static/',
        'current_name': '新闻动态',
        'id': offset,
        'news': news.objects.get(id=offset),
        'new': news.objects.all()[0:5],
        'hot': news.objects.order_by('-read')[0:5]
    }
    n = news.objects.get(id=offset)
    n.read += 1
    n.save()

    if request.session.has_key('id'):
        render['user'] = user.objects.get(id=request.session['id'])
    return render_to_response('news_view.html', render)


def activitys(request):
    render = {
        'current_name': '专题活动',
        'url': '../static/',
        'activity': activity.objects.all(),
        'new': activity.objects.all()[0:5],
        'hot': activity.objects.all()[0:5]
    }
    if request.session.has_key('id'):
        render['user'] = user.objects.get(id=request.session['id'])
    return render_to_response('activity.html', render)


def activity_view(request, offset):
    render = {
        'url': '../../static/',
        'current_name': '专题活动',
        'id': offset,
        'activity': activity.objects.get(id=offset),
        'new': activity.objects.all()[0:5],
        'hot': activity.objects.all()[0:5]
    }
    if request.session.has_key('id'):
        render['user'] = user.objects.get(id=request.session['id'])
    return render_to_response('activity_view.html', render)


def joins(request):
    render = {
        'current_name': '公益招募',
        'url': '../static/',
        'join': join.objects.all(),
        'new': join.objects.all()[0:5],
        'hot': join.objects.all()[0:5],
    }
    if request.session.has_key('id'):
        render['user'] = user.objects.get(id=request.session['id'])
    return render_to_response('join.html', render)


def join_view(request, offset):
    render = {
        'url': '../../static/',
        'current_name': '公益招募',
        'id': offset,
        'join': join.objects.get(id=offset),
        'new': join.objects.all()[0:5],
        'hot': join.objects.all()[0:5],
    }
    if request.session.has_key('id'):
        render['user'] = user.objects.get(id=request.session['id'])
    return render_to_response('join_view.html', render)


def donates(request):
    render = {
        'current_name': '乐捐',
        'url': '../static/',
        'donate': donate.objects.all(),
        'new': donate.objects.all()[0:5],
        'hot': donate.objects.all()[0:5],
    }
    if request.session.has_key('id'):
        render['user'] = user.objects.get(id=request.session['id'])
    return render_to_response('donate.html', render)


def donate_view(request, offset):
    render = {
        'url': '../../static/',
        'current_name': '乐捐',
        'id': offset,
        'donate': donate.objects.get(id=offset),
        'new': donate.objects.all()[0:5],
        'hot': donate.objects.all()[0:5],
    }
    if request.session.has_key('id'):
        render['user'] = user.objects.get(id=request.session['id'])
    return render_to_response('donate_view.html', render)


def about(request):
    render = {
        'current_name': '关于我们',
        'url': '../static/',
    }
    if request.session.has_key('id'):
        render['user'] = user.objects.get(id=request.session['id'])
    return render_to_response('about.html', render)


def contact(request):
    render = {
        'current_name': '联系我们',
        'url': '../static/',
    }
    if request.session.has_key('id'):
        render['user'] = user.objects.get(id=request.session['id'])
    return render_to_response('contact.html', render)


def test(request):
    render = {
        'url': '../static/',
        'cuttent_name': '新闻动态',
        'donate': donate.objects.all(),
        'news': news.objects.all(),
        'activity': activity.objects.all(),
        'join': join.objects.all()
    }
    if request.session.has_key('id'):
        render['user'] = user.objects.get(id=request.session['id'])
    return render_to_response('test.html', render)


def pictures(request, offset):
    render = {
        'url': '../../static/',
        'current_name': '新闻动态',
        'picture': picture.objects.get(id=offset)
    }
    if request.session.has_key('id'):
        render['user'] = user.objects.get(id=request.session['id'])
    return render_to_response('picture.html', render)


def test_plus(request, offset):
    render = {
        'url': '../../static/',
        'current_name': '新闻动态',
        'id': offset,
        'news': news.objects.get(id=offset)
    }
    if request.session.has_key('id'):
        render['user'] = user.objects.get(id=request.session['id'])
    return render_to_response('news_view.html', render)
