from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views
from .forms import *

app_name = 'marketplace_app'

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('signup/', views.signup, name="signup"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='marketplace_app/login.html', authentication_form=LoginForm), name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)