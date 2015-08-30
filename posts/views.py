# -*- coding: utf-8 -*-
from blogs.models import Blog
from posts.forms import PostCreateForm
from posts.models import Post, PUBLISHED, PUBLIC
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.db.models import Q


class PostsDetailView(View):
    def get(self, req, username, pk):
        if req.user.is_authenticated():
            posts = Post.objects.filter(pk=pk, owner=req.user)
        else:
            posts = Post.objects.filter(pk=pk, post_type=PUBLIC)

        context = {
            'post_list': posts
        }
        return render(req, 'posts/post_detail.html', context)


class PostsUserView(View):
    def get(self, req, username):
        if req.user.is_authenticated():
            if username == req.user.username:
                posts = Post.objects.filter(owner__username=username)
            else:
                posts = Post.objects.filter(owner__username=username, post_type=PUBLIC)
        else:
            posts = Post.objects.filter(owner__username=username, post_type=PUBLIC)

        # posts = Post.objects.all()

        context = {
            'post_list': posts
        }
        return render(req, 'blogs/home.html', context)

class PostsUserViewAll(View):
    def get(self, req):

        posts = Post.objects.filter(post_type=PUBLIC)

        # posts = Post.objects.all()

        context = {
            'post_list': posts
        }
        return render(req, 'blogs/home.html', context)

class PostCreateView(View):
    @method_decorator(login_required())
    def get(self, req):
        """
        Muestra un form para crear un post y lo crea si la petición es POST
        :param req: HttpRequest
        :return: HttpResponse
        """
        error_messages = []
        form = PostCreateForm()

        context = {
            'form': form
        }
        return render(req, 'posts/new_post.html', context)

    @method_decorator(login_required())
    def post(self, req):
        """
        Muestra un form para crear un post y lo crea si la peticion es POST
        :param req: HttpRequest
        :return: HttpResponse
        """
        error_messages = []
        success_message = ''

        # Creamos owner y se lo pasamos al form con un objeto pre-establecido
        post_with_owner = Post()
        post_with_owner.owner = req.user
        post_with_owner.blog = Blog.objects.filter(owner=req.user)[0]

        form = PostCreateForm(req.POST, instance=post_with_owner)
        if form.is_valid():

            new_post = form.save()
            form = PostCreateForm()
            success_message = u'Post guardado con éxito! '
            success_message += u'<a href="{0}">'.format(reverse('post_detail', args=[req.user.username, new_post.pk]))
            success_message += u'(ver post)</a>'
        else:
            error_messages.append(u'Formulario incompleto.')

        context = {
            'form': form,
            'success_message': success_message
        }
        return render(req, 'posts/new_post.html', context)


# query sets
class PostQuerySet(object):

    def get_post_queryset(self, req):
        search_title = self.request.query_params.get('title', None)
        search_body = self.request.query_params.get('content', None)
        order_by = self.request.query_params.get('content', None)

        if not req.user.is_authenticated():
            posts = Post.objects.filter(status=PUBLISHED, post_type=PUBLIC).order_by('-created_at')
        elif req.user.is_superuser:  # es super admin
            posts = Post.objects.all().order_by('-created_at')
        else:
            posts = Post.objects.filter(Q(owner=req.user) | Q(status=PUBLISHED) | Q(blog__owner=req.user)).order_by('-created_at')

        # filters
        if search_title:
            posts = posts.filter(title__icontains=search_title)

        if search_body:
            posts = posts.filter(body__icontains=search_body)

        if order_by:
            if order_by == 'asc':
                posts = posts.order_by('created_at')
            else:
                posts = posts.order_by('-created_at')

        return posts
