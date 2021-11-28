from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, ArticlesCreateFrom
from .models import Article


class UserDetailsView(DetailView):
    model = User
    template_name = 'main/user.html'
    pk_url_kwarg = 'user_id'
    context_object_name = 'user'


class HomePage(TemplateView):
    template_name = 'main/home_page.html'

    def get(self, request, *args, **kwargs):
        login_form = AuthenticationForm
        registration_form = UserRegistrationForm
        context = self.get_context_data(**kwargs)
        context['login_form'] = login_form
        context['registration_form'] = registration_form
        return self.render_to_response(context)


def home_page(request):
    return render(request, 'main/home_page.html')


def about_page(request):
    return render(request, 'main/about_page.html')


class ArticlesPage(ListView):
    model = Article
    template_name = 'main/articles_page.html'
    context_object_name = 'articles'
    paginate_by = 10
    queryset = Article.objects.all()

    def get_queryset(self):
        find = self.request.GET.get('find')
        if find is None:
            return self.model.objects.all()
        return self.model.objects.filter(title__icontains=find)


def articles_page(request):
    return render(request, 'main/articles_page.html')


class RegistrationForm(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for error_key in self.get_form().errors:
            context['message'] = self.get_form().errors[error_key][0]
            break
        return context


class ArticleCreateFormView(CreateView):
    form_class = ArticlesCreateFrom
    template_name = 'main/article_creation.html'
    success_url = reverse_lazy('articles')


class ArticleDetailsView(DetailView):
    model = Article
    template_name = 'main/article.html'
    pk_url_kwarg = 'article_id'
    context_object_name = 'article'


class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticlesCreateFrom
    template_name = 'main/article_update.html'
    pk_url_kwarg = 'article_id'


class ArticleDelete(DeleteView):
    model = Article
    template_name = 'main/article_delete.html'
    pk_url_kwarg = 'article_id'
    success_url = reverse_lazy('articles')
