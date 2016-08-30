#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Created by zhoupan on 8/30/16.
"""
from django import forms


class ContactForm(forms.Form):
    nick_name = forms.CharField(min_length=2, max_length=20)
    real_name = forms.CharField(min_length=2, max_length=20)
    phone = forms.CharField(min_length=11, max_length=11)
    email = forms.EmailField()
    passwd = forms.CharField(min_length=2, max_length=20)
    birthday = forms.CharField(max_length=10, black=True)
    address = forms.CharField(max_length=40, black=True)
    education = forms.IntegerField()
    about = forms.Textarea()