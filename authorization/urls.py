from django.urls import path, include
from django.views.decorators.cache import cache_page
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('user/<int:user_id>', cache_page(5 * 60)(views.UserDetailsView.as_view()), name='user_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration', views.RegistrationForm.as_view(), name='registration'),
    path('about', views.AboutPage.as_view(), name='about'),
    path('articles', views.ArticlesPage.as_view(), name='articles'),
    path('articles/create', views.ArticleCreateFormView.as_view(), name='article_create'),
    path('articles/<int:article_id>', cache_page(60)(views.ArticleDetailsView.as_view()), name='article_page'),
    path('articles/<int:article_id>/update', views.ArticleUpdate.as_view(), name='article_update'),
    path('articles/<int:article_id>/delete', views.ArticleDelete.as_view(), name='article_delete'),
]
