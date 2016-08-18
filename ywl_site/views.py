#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from ywl_site.models import *


def index(request):
    return render_to_response('index.html', {
        'current_name': '首页',
        'url': '../static/',
        'donate': donate.objects.all(),
        'news': news.objects.all(),
        'activity': activity.objects.all(),
        'join': join.objects.all(),
        'about': picture.objects.all()[0:4],
        'picture': picture.objects.all(),
    }
                              )


def newss(request):
    return render_to_response('news.html', {
        'current_name': '新闻动态',
        'url': '../static/',
        'news': news.objects.all(),
        'new': news.objects.all()[0:5],
        'hot': news.objects.order_by('read')[0:5]
    }
                              )


def news_view(request, offset):
    return render_to_response('news_view.html', {
        'url': '../../static/',
        'current_name': '新闻动态',
        'id': offset,
        'news': news.objects.get(id=offset),
        'new': news.objects.all()[0:5],
        'hot': news.objects.order_by('read')[0:5]
    }
                              )

def activitys(request):
    return render_to_response('activity.html', {
        'current_name': '专题活动',
        'url': '../static/',
        'activity': activity.objects.all(),
        'new': activity.objects.all()[0:5],
        'hot': activity.objects.all()[0:5]
    }
                              )


def activity_view(request, offset):
    return render_to_response('activity_view.html', {
        'url': '../../static/',
        'current_name': '专题活动',
        'id': offset,
        'activity': activity.objects.get(id=offset),
        'new': activity.objects.all()[0:5],
        'hot': activity.objects.all()[0:5]
    }
                              )


def joins(request):
    return render_to_response('join.html', {
        'current_name': '公益招募',
        'url': '../static/',
        'join': join.objects.all(),
        'new': join.objects.all()[0:5],
        'hot': join.objects.all()[0:5],
    }
                              )


def join_view(request, offset):
    return render_to_response('join_view.html', {
        'url': '../../static/',
        'current_name': '公益招募',
        'id': offset,
        'join': join.objects.get(id=offset),
        'new': join.objects.all()[0:5],
        'hot': join.objects.all()[0:5],
    }
                              )


def donates(request):
    return render_to_response('donate.html', {
        'current_name': '乐捐',
        'url': '../static/',
        'donate': donate.objects.all(),
        'new': donate.objects.all()[0:5],
        'hot': donate.objects.all()[0:5],
    }
                              )


def donate_view(request, offset):
    return render_to_response('donate_view.html', {
        'url': '../../static/',
        'current_name': '乐捐',
        'id': offset,
        'donate': donate.objects.get(id=offset),
        'new': donate.objects.all()[0:5],
        'hot': donate.objects.all()[0:5],
    }
                              )


def about(request):
    return render_to_response('about.html', {
        'current_name': '关于我们',
        'url': '../static/',
    }
                              )


def contact(request):
    return render_to_response('contact.html', {
        'current_name': '联系我们',
        'url': '../static/',
    }
                              )


def test(request):
    return render_to_response('test.html', {
        'url': '../static/',
        'cuttent_name': '新闻动态',
        'donate': donate.objects.all(),
        'news': news.objects.all(),
        'activity': activity.objects.all(),
        'join': join.objects.all()
    }
                              )


def test_plus(request, offset):
    return render_to_response('news_view.html', {
        'url': '../../static/',
        'current_name': '新闻动态',
        'id': offset,
        'news': news.objects.get(id=offset)
    }
                              )
