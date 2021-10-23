from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('user/<int:user_id>', views.UserDetailsView.as_view(), name='user_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration', views.RegistrationForm.as_view(), name='registration'),
    path('about', views.about_page, name='about'),
    path('articles', views.ArticlesPage.as_view(), name='articles'),
]
