from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import UserRegistrationForm


class UserDetailsView(DetailView):
    model = User
    template_name = 'main/user.html'
    pk_url_kwarg = 'user_id'
    context_object_name = 'user'


def home_page(request):
    return render(request, 'main/home_page.html')


def about_page(request):
    return render(request, 'main/about_page.html')


def articles_page(request):
    return render(request, 'main/articles_page.html')


class RegistrationForm(FormView):
    form_class = UserRegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for error_key in self.get_form().errors:
            context['message'] = self.get_form().errors[error_key][0]
            break
        return context


'''def registration_page(request):
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
    return render(request, 'registration/registration.html', data)'''
