# -*- coding: utf-8 -*-
from blogs.views import HomeView, BlogListView, BlogUserView
from django.conf.urls import url


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='blogs_home'),
    url(r'^blogs$', BlogListView.as_view(), name='blogs_list'),
    url(r'blogs/(?P<username>[-\w]+)/$', BlogUserView.as_view(), name='user_blogs'),
]
