from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.models import User
from .forms import UserRegistrationForm


class UserDetailsView(DetailView):
    model = User
    template_name = 'main/user.html'
    context_object_name = 'user'


def home_page(request):
    return render(request, 'main/home_page.html')


def about_page(request):
    return render(request, 'main/about_page.html')


def articles_page(request):
    return render(request, 'main/articles_page.html')


def registration_page(request):
    message = ''

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            message = 'Wrong form!'

    form = UserRegistrationForm()

    data = {
        'form': form,
        'message': message,
    }
    return render(request, 'registration/registration.html', data)
