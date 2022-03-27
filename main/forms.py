from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUser(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    email = forms.CharField()
    is_active = forms.CharField()
    date_joined = forms.CharField()
    # last_login = forms.CharField()

    class Meta:
        model = User
        fields = ('username',
                  'password1',
                  'password2',
                  'email',
                  'is_active',
                  'date_joined',
                  # 'last_login'
                  )
