# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from users.api import UserViewSet

router = DefaultRouter()
router.register('user', UserViewSet, base_name='user')

urlpatterns = [
    url(r'1.0/', include(router.urls)),  # include de las url's router
]
