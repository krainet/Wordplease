# -*- coding: utf-8 -*-
from posts.views import PostCreateView, PostsUserViewAll
from posts.views import PostsUserView, PostsDetailView
from django.conf.urls import url


urlpatterns = [
    url(r'posts/$', PostsUserViewAll.as_view(), name='user_posts_single'),
    url(r'posts/(?P<username>[-\w]+)/$', PostsUserView.as_view(), name='user_posts'),
    url(r'posts/(?P<username>[-\w]+)/(?P<pk>[0-9]+)$', PostsDetailView.as_view(), name='post_detail'),
    url(r'^new-post$', PostCreateView.as_view(), name='post_create'),
]
