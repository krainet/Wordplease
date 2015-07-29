# -*- coding: utf-8 -*-
__author__ = 'hadock'
from rest_framework.permissions import BasePermission

class PostPermission(BasePermission):
    def has_permission(self, request, view):
        """
        Define si el user autenticado en request.user tiene permiso para realizar una accion
        ya sea (get , post , put o delete)
        :param request:
        :param view:
        :return:
        """

        if view.action == 'create':
            return True
        elif request.user.is_superuser:
            return True
        elif view.action in ['retrieve', 'update', 'destroy']:
            return True
        else:
            # Bloqueo acceso a /users/ si no es superadmin
            return False

    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario autenticado (req.user) tiene permiso para realizar la accion (get post...)
        sobre el objeto obj
        :param request:
        :param view:
        :param obj:
        :return:
        """
        # si es superadmin , o el usuario autenticado intenta hacer
        # GET , PUT o DELETE sobre su mismo perfil
        return request.user.is_superuser or request.user == obj
