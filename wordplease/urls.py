# -*- coding: utf-8 -*-
from blogs.api import BlogListAPI, BlogDetailAPI
# from posts.api import PostListAPI, PostDetailAPI
from blogs.views import HomeView, BlogListView, BlogUserView, PostCreateView
from posts.api import PostViewSet
from posts.views import PostsUserView, PostsDetailView
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from users.api import UserDetailAPI, UserListAPI
from users.views import LoginView, LogoutView, SignupView
from users import urls as user_urls
from blogs import urls as blog_urls
from posts import urls as post_urls


# Router de rest framework
router = DefaultRouter()

# registro ruta post
router.register('api/1.0/post', PostViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(user_urls)),
    url(r'', include(blog_urls)),
    url(r'', include(post_urls))
]
