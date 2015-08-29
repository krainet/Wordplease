# -*- coding: utf-8 -*-
from django.contrib import admin
from blogs.models import Blog

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'status')
    list_filter = ('owner', 'status')
    search_fields = ('title',)

    def owner_name(self, obj):
        return obj.owner.first_name + u' ' + obj.owner.last_name

    owner_name.short_description = u'Blog Owner'
    owner_name.admin_order_field = 'owner'

admin.site.register(Blog)
