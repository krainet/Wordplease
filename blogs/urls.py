# -*- coding: utf-8 -*-
from blogs.views import HomeView, BlogListView, BlogUserView, BlogByIdView
from django.conf.urls import url


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='blogs_home'),
    url(r'^blogs$', BlogListView.as_view(), name='blogs_list'),
    url(r'blogs/(?P<username>[-\w]+)/$', BlogUserView.as_view(), name='user_blogs'),
    url(r'blogs/(?P<username>[-\w]+)/(?P<pk>[0-9]+)/$', BlogByIdView.as_view(), name='blog_detail'),
]
