from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'conversation'

urlpatterns = [
    path('new/<int:item_pk>/', views.new_conversation, name='new')
]