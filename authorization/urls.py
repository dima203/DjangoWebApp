from django.urls import path, include
from django.views.decorators.cache import cache_page
from django.contrib.auth import views as auth_views
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('user/<int:user_id>', cache_page(5 * 60)(views.UserDetailsView.as_view()), name='user_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration', views.RegistrationForm.as_view(), name='registration'),
    path('accounts/url_reg', views.url_reg, name='url_reg'),
    path('about', views.AboutPage.as_view(), name='about'),
    path('articles', views.ArticlesPage.as_view(), name='articles'),
    path('articles/create', views.ArticleCreateFormView.as_view(), name='article_create'),
    path('articles/<int:article_id>', views.ArticleDetailsView.as_view(), name='article_page'),
    path('articles/<int:article_id>/update', views.ArticleUpdate.as_view(), name='article_update'),
    path('articles/<int:article_id>/delete', views.ArticleDelete.as_view(), name='article_delete'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
