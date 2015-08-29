# -*- coding: utf-8 -*-
from blogs.models import Blog

__author__ = 'hadock'
from django import forms
from posts.models import Post


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ['owner', 'status', 'blog']

    # TODO Conseguir que el form solo muestre los blogs del user
    # def __init__(self, *args, **kwargs):
    #     super(PostCreateForm, self).__init__(*args, **kwargs)
    #     if self.instance:
    #         self.fields['blog'].queryset = Blog.objects.filter(blog=self.instance)


