# -*- coding: utf-8 -*-
from blogs.serializers import PostListSerializer, PostSerializer, BlogSerializer, BlogListSerializer
from blogs.views import PostQuerySet, BlogQuerySet

__author__ = 'hadock'
from blogs.models import Post, Blog
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostListAPI(PostQuerySet, ListCreateAPIView):
    queryset = Post.objects.all()

    permission_classes = (IsAuthenticatedOrReadOnly,)

    #  Al sobreescribir este método podemos usar un serializador u
    #  otro en funcion del metodo de la vista generica ListCreateApiView

    def get_serializer_class(self):
        return PostSerializer if self.request.method == 'POST' else PostListSerializer

    def get_queryset(self):
        return self.get_post_queryset(self.request)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetailAPI(PostQuerySet, RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.get_post_queryset(self.request)


class BlogListAPI(BlogQuerySet, ListCreateAPIView):
    queryset = Blog.objects.all()

    permission_classes = (IsAuthenticatedOrReadOnly,)

    #  Al sobreescribir este método podemos usar un serializador u
    #  otro en funcion del metodo de la vista generica ListCreateApiView

    def get_serializer_class(self):
        return BlogSerializer if self.request.method == 'POST' else BlogListSerializer

    def get_queryset(self):
        return self.get_blog_queryset(self.request)

    def perform_create(self, serializer):
        serializer.save(blog_url='http://hola.com')

class BlogDetailAPI(BlogQuerySet, RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_fields = ('username',)

    def get_queryset(self):
        return self.get_blog_queryset(self.request)
