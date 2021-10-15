from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('user/<int:pk>', views.UserDetailsView.as_view(), name='user_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration', views.registration_page, name='registration'),
    path('about', views.about_page, name='about'),
    path('articles', views.articles_page, name='articles'),
]
