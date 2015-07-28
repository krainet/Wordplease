# -*- coding: utf-8 -*-
__author__ = 'hadock'
from django import forms
from posts.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['owner', 'status']

