# -*- coding: utf-8 -*-
__author__ = 'hadock'
from django import forms
from blogs.models import Post, Blog


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['owner']


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['owner']
