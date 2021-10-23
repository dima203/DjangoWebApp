from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-input'}))

    def clean_email(self):
        data = self.cleaned_data['email']
        users = User.objects.filter(email=data).exists()
        if users:
            raise forms.ValidationError('Пользователь с таким адресом электронной почты уже зарегистрирован')
        return data
