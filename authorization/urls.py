from django.urls import path, include
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path('', cache_page(15 * 60)(views.home_page), name='home'),
    path('user/<int:user_id>', cache_page(5 * 60)(views.UserDetailsView.as_view()), name='user_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration', views.RegistrationForm.as_view(), name='registration'),
    path('about', cache_page(15 * 60)(views.about_page), name='about'),
    path('articles', views.ArticlesPage.as_view(), name='articles'),
    path('articles/create', views.ArticleCreateFormView.as_view(), name='article_create'),
    path('articles/<int:article_id>', cache_page(60)(views.ArticleDetailsView.as_view()), name='article_page'),
    path('articles/<int:article_id>/update', views.ArticleUpdate.as_view(), name='article_update'),
    path('articles/<int:article_id>/delete', views.ArticleDelete.as_view(), name='article_delete'),
]
