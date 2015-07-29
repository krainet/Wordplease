# -*- coding: utf-8 -*-
from blogs.api import BlogViewSet
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('blog', BlogViewSet)

urlpatterns = [
    url(r'1.0/', include(router.urls)),  # include de las url's router
]
