# -*- coding: utf-8 -*-
__author__ = 'hadock'
from rest_framework.permissions import BasePermission

class BlogPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif view.action in ['retrieve', 'list']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.acttion in ['list', 'retrieve']:
            return True

        return request.user.is_superuser or request.user == obj
