#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Create your views here.
from django.shortcuts import render_to_response

from ywl_site.models import *


def index(request):
    return render_to_response('index.html', {
        'current_name': '首页',
        'url': '../static/',
        'donate': donate.objects.all(),
        'news': news.objects.all(),
        'activity': activity.objects.all(),
        'join': join.objects.all()
    }
)


def newss(request):
    return render_to_response('news.html', {'current_name': '新闻动态', 'url': '../static/', 'news': news.objects.all()})


def news_view(request, offset):
    return render_to_response('news_view.html', {'url': '../../static/', 'current_name': '新闻动态', 'id': offset,
                                                 'news': news.objects.get(id=offset)})


def activitys(request):
    return render_to_response('activity.html',
                              {'current_name': '专题活动', 'url': '../static/', 'activity': activity.objects.all()})


def activity_view(request, offset):
    return render_to_response('activity_view.html', {'url': '../../static/', 'current_name': '专题活动', 'id': offset,
                                                'activity': activity.objects.get(id=offset)})


def test(request):
    return render_to_response('test.html',
                              {'url': '../static/', 'cuttent_name': '新闻动态', 'donate': donate.objects.all(),
                               'news': news.objects.all(), 'activity': activity.objects.all(),
                               'join': join.objects.all()})


def test_plus(request, offset):
    return render_to_response('news_view.html', {'url': '../../static/', 'current_name': '新闻动态', 'id': offset,
                                                 'news': news.objects.get(id=offset)})
