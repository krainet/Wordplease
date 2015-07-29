# -*- coding: utf-8 -*-
from posts.api import PostViewSet
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('post', PostViewSet)


urlpatterns = [
    url(r'1.0/', include(router.urls)),
]
