# -*- coding: utf-8 -*-
from blogs.views import PostCreateView
from posts.views import PostsUserView, PostsDetailView
from django.conf.urls import include, url


urlpatterns = [
    # Posts
    url(r'posts/(?P<username>[-\w]+)/$', PostsUserView.as_view(), name='user_posts'),
    url(r'posts/(?P<username>[-\w]+)/(?P<pk>[0-9]+)$', PostsDetailView.as_view(), name='post_detail'),

    # Post Create
    url(r'^new-post$', PostCreateView.as_view(), name='post_create'),
]
