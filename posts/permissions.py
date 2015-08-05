# -*- coding: utf-8 -*-
__author__ = 'hadock'
from rest_framework.permissions import BasePermission

class PostPermission(BasePermission):
    def has_permission(self, request, view):

        if request.user.is_superuser:
            return True
        elif view.action in ['retrieve', 'destroy', 'list']:
            return True
        elif view.action in ['create', 'update'] and request.user.is_authenticated():
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True
        elif view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['destroy', 'update'] and request.user == obj.owner:
            return True
        else:
            return False

        # return request.user.is_superuser or request.user == obj.owner
