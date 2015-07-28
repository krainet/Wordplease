# -*- coding: utf-8 -*-
from blogs.views import PostCreateView
from posts.api import PostViewSet
from posts.views import PostsUserView, PostsDetailView
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter


# Router de rest framework
router = DefaultRouter()

# registro ruta post
router.register('api/1.0/post', PostViewSet)

urlpatterns = [
    # Posts
    url(r'posts/(?P<username>[-\w]+)/$', PostsUserView.as_view(), name='user_posts'),
    url(r'posts/(?P<username>[-\w]+)/(?P<pk>[0-9]+)$', PostsDetailView.as_view(), name='post_detail'),

    # Post Create
    url(r'^new-post$', PostCreateView.as_view(), name='post_create'),

    # urls api posts -> con viewSet y router
    url(r'', include(router.urls)),  # include de las url's router
]
