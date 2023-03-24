from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView,\
    PasswordChangeDoneView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, ArticlesCreateFrom
from .models import Article


login_form = AuthenticationForm
registration_form = UserRegistrationForm
extra_context = {'login_form': login_form, 'registration_form': registration_form}
LoginView.extra_context = extra_context
LogoutView.extra_context = extra_context
PasswordChangeView.extra_context = extra_context
PasswordResetView.extra_context = extra_context
PasswordChangeDoneView.extra_context = extra_context
PasswordResetDoneView.extra_context = extra_context
PasswordResetConfirmView.extra_context = extra_context
PasswordResetCompleteView.extra_context = extra_context


class UserDetailsView(DetailView):
    model = User
    template_name = 'main/user.html'
    pk_url_kwarg = 'user_id'
    context_object_name = 'user'
    extra_context = extra_context


class HomePage(TemplateView):
    template_name = 'main/home_page.html'
    extra_context = extra_context


class AboutPage(TemplateView):
    template_name = 'main/about_page.html'
    extra_context = extra_context


class ArticlesPage(ListView):
    model = Article
    template_name = 'main/articles_page.html'
    context_object_name = 'articles'
    paginate_by = 10
    queryset = Article.objects.all()
    login_form = AuthenticationForm
    registration_form = UserRegistrationForm
    extra_context = {'login_form': login_form, 'registration_form': registration_form}

    def get_queryset(self):
        find = self.request.GET.get('find')
        if find is None:
            return self.model.objects.all()
        return self.model.objects.filter(title__icontains=find)


class RegistrationForm(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('home')
    extra_context = extra_context

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
    extra_context = extra_context

    def post(self, request, *args, **kwargs):
        form = ArticlesCreateFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ArticleDetailsView(DetailView):
    model = Article
    template_name = 'main/article.html'
    pk_url_kwarg = 'article_id'
    context_object_name = 'article'
    extra_context = extra_context


class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticlesCreateFrom
    template_name = 'main/article_update.html'
    pk_url_kwarg = 'article_id'
    extra_context = extra_context

    def post(self, request, *args, **kwargs):
        form = ArticlesCreateFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ArticleDelete(DeleteView):
    model = Article
    template_name = 'main/article_delete.html'
    pk_url_kwarg = 'article_id'
    success_url = reverse_lazy('articles')
    extra_context = extra_context
