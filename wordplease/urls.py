# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from users import urls as user_urls
from blogs import urls as blog_urls
from posts import urls as post_urls
from users import api_urls as user_api_urls
from blogs import api_urls as blog_api_urls
from posts import api_urls as post_api_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(user_urls)),
    url(r'', include(blog_urls)),
    url(r'', include(post_urls)),

    url(r'api/', include(user_api_urls)),
    url(r'api/', include(blog_api_urls)),
    url(r'api/', include(post_api_urls))
]
