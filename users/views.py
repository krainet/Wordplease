# -*- coding: utf-8 -*-
import logging
from blogs.models import Blog
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from users.forms import LoginForm, UserCreateForm
from django.views.generic import View

logger = logging.getLogger(__name__)

class LoginView(View):
    def get(self, request):
        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        error_messages = []

        # Using form instade of direct request.POST
        # username = request.POST.get('usr', '')
        # password = request.POST.get('pwd', '')
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')

            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append('Nombre de usuario o clave incorrectos')
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect(request.GET.get('next','blogs_home'))
                else:
                    error_messages.append('El usuario no esta activo')

        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)


class LogoutView(View):
    def get(self, request):
        django_logout(request)
        return redirect('blogs_home')


class SignupView(View):
    def get(self, req):
        form = UserCreateForm()
        context = {
            'form': form
        }
        return render(req, 'users/signup.html', context)

    def post(self, req):
        error_messages = []
        success_message = ''
        user = User()
        form = UserCreateForm(req.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(new_user.password)
            new_user.save()
            form = UserCreateForm()
            success_message = u'User creado con éxito! '

            # blog for this user.
            blog = Blog(owner=new_user)
            if not req.POST.get('blog_name'):
                blog.name = 'Blog de ' + new_user.username
            else:
                blog.name = req.POST.get('blog_name')

            if not req.POST.get('blog_sdescription'):
                blog.short_description = 'Bienvenido al blog de ' + new_user.username
            else:
                blog.short_description = req.POST.get('blog_sdescription')
            blog.save()
        else:
            error_messages.append(u'Formulario incompleto.')

        context = {
            'form': form,
            'success_message': success_message,
            'error_messages': error_messages
        }
        return render(req, 'users/signup.html', context)


def prueba(req):
    context = dict(myvar='hola')
    return render(req, 'users/prueba.html', context)


