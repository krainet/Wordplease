# -*- coding: utf-8 -*-
from blogs.api import PostListAPI, PostDetailAPI, BlogListAPI, BlogDetailAPI
from blogs.views import HomeView, BlogListView, PostsDetailView, PostsUserView, PostCreateView, BlogUserView
from django.conf.urls import include, url
from django.contrib import admin
from users.api import UserDetailAPI, UserListAPI
from users.views import LoginView, LogoutView, SignupView



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),



    # Test URL
    url(r'^testurl$', 'blogs.views.prueba', name='blogs_prueba'),

    # Base URL (home)
    url(r'^$', HomeView.as_view(), name='blogs_home'),

    # Blogs & Posts
    url(r'^blogs$', BlogListView.as_view(), name='blogs_list'),
    url(r'blogs/(?P<username>[-\w]+)/$', BlogUserView.as_view(), name='user_blogs'),
    url(r'posts/(?P<username>[-\w]+)/$', PostsUserView.as_view(), name='user_posts'),
    url(r'posts/(?P<username>[-\w]+)/(?P<pk>[0-9]+)$', PostsDetailView.as_view(), name='post_detail'),

    # Post Create
    url(r'^new-post$', PostCreateView.as_view(), name='post_create'),

    # Users
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),
    url(r'^signup$', SignupView.as_view(), name='users_signup'),

    # urls api users
    url(r'^api/1.0/users/$', UserListAPI.as_view(), name='user_list_api'),
    url(r'^api/1.0/users/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='user_detail_api'),

    # urls api posts
    url(r'^api/1.0/posts/$', PostListAPI.as_view(), name='posts_list_api'),
    url(r'^api/1.0/posts/(?P<pk>[0-9]+)$', PostDetailAPI.as_view(), name='post_detail_api'),

    # urls api blogs
    url(r'^api/1.0/blogs/$', BlogListAPI.as_view(), name='blogs_list_api'),
    url(r'^api/1.0/blogs/(?P<username>[-\w]+)$', BlogDetailAPI.as_view(), name='blogs_detail_api')
    # url(r'^api/1.0/blogs/(?P<pk>[0-9]+)$', BlogDetailAPI.as_view(), name='blogs_detail_api')


]
