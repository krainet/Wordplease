# -*- coding: utf-8 -*-
from django.contrib.auth.models import User

__author__ = 'hadock'
from django import forms

class LoginForm(forms.Form):

    usr = forms.CharField(label='Username')
    pwd = forms.CharField(label='Password', widget=forms.PasswordInput)


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password',]

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', ]:
            self.fields[fieldname].help_text = None

        for fieldname in ['username', 'email', 'password']:
            self.fields[fieldname].required = True