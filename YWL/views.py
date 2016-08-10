#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
    Created by zhoupan on 8/9/16.
"""
from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html')
def news(request):
    return render_to_response('news_test.html')
