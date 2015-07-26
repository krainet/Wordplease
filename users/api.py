# -*- coding: utf-8 -*-
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from users.permissions import UserPermission

__author__ = 'hadock'
from django.contrib.auth.models import User
# from rest_framework.views import APIView
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import GenericAPIView

class UserListAPI(GenericAPIView):

    # serializer_class = UserSerializer
    permission_classes = (UserPermission,)

    def get(self, req):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        serialized_users = serializer.data # en data van los datos...
        return Response(serialized_users)

    def post(self, req):
        serializer = UserSerializer(data=req.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        return UserSerializer

class UserDetailAPI(GenericAPIView):

    permission_classes = (UserPermission,)

    def get(self, req, pk):
        user = get_object_or_404(User, pk=pk)
        # aqui y siempre que declaremos los metodos nosotros , nos toca comprobar a mano
        # si el usuario tiene permiso
        self.check_object_permissions(req, user)  # checar permisos
        return Response(UserSerializer(user).data)

    def put(self, req, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(req, user)  # permisos a mano
        serializer = UserSerializer(instance=user, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, req, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(req, user)  # permisos a manija
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
