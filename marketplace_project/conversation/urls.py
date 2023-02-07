from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

app_name = 'conversation'

urlpatterns = [
    path('new/<int:item_pk>/', views.new_conversation, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('', views.inbox, name='inbox'),
]