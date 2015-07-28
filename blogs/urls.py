# -*- coding: utf-8 -*-
from blogs.api import BlogListAPI, BlogDetailAPI
from blogs.views import HomeView, BlogListView, BlogUserView, PostCreateView
from django.conf.urls import url


urlpatterns = [
    # Base URL (home)
    url(r'^$', HomeView.as_view(), name='blogs_home'),

    # Blogs
    url(r'^blogs$', BlogListView.as_view(), name='blogs_list'),
    url(r'blogs/(?P<username>[-\w]+)/$', BlogUserView.as_view(), name='user_blogs'),

    # urls api blogs
    url(r'^api/1.0/blogs/$', BlogListAPI.as_view(), name='blogs_list_api'),
    # url(r'^api/1.0/blogs/(?P<username>[-\w]+)$', BlogDetailAPI.as_view(), name='blogs_detail_api')
    url(r'^api/1.0/blogs/(?P<pk>[0-9]+)$', BlogDetailAPI.as_view(), name='blogs_detail_api')
]
