# -*- coding: utf-8 -*-
__author__ = 'hadock'
from django import forms
from blogs.models import Blog


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['owner']
