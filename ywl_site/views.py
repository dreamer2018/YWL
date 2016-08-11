#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Create your views here.
from django.shortcuts import render_to_response

from ywl_site.models import *


def index(request):
    return render_to_response('index.html', {'current_name': '首页'})


def newss(request):
    return render_to_response('news_test.html', {'current_name': '新闻动态'})


def test(request):
    return render_to_response('test.html',
                              {'cuttent_name': '新闻动态', 'donate': donate.objects.all(),
                               'news': news.objects.all(), 'activity': activity.objects.all(),
                               'join': join.objects.all()})
