from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput

from .models import Article


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-input'}))

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
        fields = ['title', 'content', 'author']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'class': 'form-input'}),
            'author': forms.TextInput(attrs={'class': 'form-input'}),
        }
