from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, Textarea, URLInput, FileInput

from .models import Article

from material import *


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='E-mail')

    layout = Layout('username', 'email',
                    Row('password1', 'password2'))

    def clean_email(self):
        data = self.cleaned_data['email']
        users = User.objects.filter(email=data).exists()
        if users:
            raise forms.ValidationError('Пользователь с таким адресом электронной почты уже зарегистрирован')
        return data


class ArticlesCreateFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Article
        fields = ['poster', 'title', 'content', 'author', 'next_article', 'prev_article']

        widgets = {
            'poster': FileInput(attrs={'class': 'form-input'}),
            'title': TextInput(attrs={'class': 'form-input'}),
            'content': Textarea(attrs={'class': 'form-input'}),
            'next_article': TextInput(attrs={'class': 'form-input'}),
            'prev_article': TextInput(attrs={'class': 'form-input'}),
            'author': TextInput(attrs={'class': 'form-input'}),
        }
