# -*- coding: utf-8 -*-
from blogs.models import PUBLISHED, Blog, ACTIVE
from posts.forms import PostCreateForm
from posts.models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.db.models import Q


class HomeView(View):
    def get(self, req):
        posts = Post.objects.filter(status=PUBLISHED).order_by('-created_at')
        context = {
            'post_list': posts
        }
        return render(req, 'blogs/home.html', context)


class BlogListView(View):
    def get(self, req):
        blogs = Blog.objects.filter(status=ACTIVE).order_by('-created_at')

        context = {
            'blog_list': blogs
        }
        return render(req, 'blogs/blogs_list.html', context)


class BlogUserView(View):
    def get(self, req, username):
        blogs = Blog.objects.filter(owner__username=username)
        # posts = Post.objects.all()

        context = {
            'blog_list': blogs
        }
        return render(req, 'blogs/blogs_list.html', context)


class BlogQuerySet(object):
    def get_blog_queryset(self, req):
        if not req.user.is_authenticated():
            blogs = Blog.objects.filter(status=ACTIVE).order_by('-created_at')
        elif req.user.is_superuser:  # es super admin
            blogs = Blog.objects.all()
        else:
            blogs = Blog.objects.filter(Q(owner=req.user) | Q(state=ACTIVE))

        return blogs


