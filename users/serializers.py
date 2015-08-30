# -*- coding: utf-8 -*-
from blogs.models import Blog
from django.contrib.auth.models import User
from wordplease.settings import PH_IMAGES

__author__ = 'hadock'
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    # parecido a un form

    id = serializers.ReadOnlyField()  # campo solo lectura , no se indica id al crear user
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def getExtraField(self, fieldName):
        req = self.context.get('request', None)
        if req is not None:
            return req.data.get(fieldName)
        else:
            return None

    def create(self, validated_data):
        """
        Crea un User a partir de validated_data (valores deserializados)
        :param validated_data:
        :return:
        """

        # extra fields from context
        blog_title = self.getExtraField('blog_title')
        blog_description = self.getExtraField('blog_description')

        instance = User()
        user = self.update(instance, validated_data)
        if user:
            Blog.objects.create(owner=user, title=blog_title, short_description=blog_description, image_url=PH_IMAGES)
        return user

    def update(self, instance, validated_data):
        """
        Actualiza uns instancia User a partir de los datos del diccionario
        validate_data que contiene datos deserializados
        :param instance:
        :param validated_data:
        :return:
        """
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.set_password(validated_data.get('password'))
        instance.email = validated_data.get('email')
        instance.save()
        return instance

    def validate_username(self, data):
        """
        Validamos si un user existe
        :param data:
        :return:
        """

        users = User.objects.filter(username=data)
        if users:
            raise serializers.ValidationError(u'Ya existe un usuario con este username')

        # caso CREATE (no hay instancia)  comprobar si hay usuario con ese username
        if not self.instance:
            return data
        elif not self.instance and len(users) != 0:
            raise serializers.ValidationError(u'Ya existe un usuario con este username')
        # Si estoy actualizando, el nuevo username es diferente al de la instancia (está cambiando el username)
        # y existen usuarios ya registrados con el nuevo username
        elif self.instance.username != data and len(users) != 0:
            raise serializers.ValidationError(u'Ya existe un usuario con este username')
        else:
            return data
