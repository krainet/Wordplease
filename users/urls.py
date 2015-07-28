# -*- coding: utf-8 -*-
from django.conf.urls import url
from users.api import UserDetailAPI, UserListAPI
from users.views import LoginView, LogoutView, SignupView

urlpatterns = [
    # Users
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),
    url(r'^signup$', SignupView.as_view(), name='users_signup'),

    # urls api users
    url(r'^api/1.0/users/$', UserListAPI.as_view(), name='user_list_api'),
    url(r'^api/1.0/users/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='user_detail_api'),
]
