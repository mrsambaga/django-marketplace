from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('items/', views.items, name='items'),
    path('items/<int:pk>/', views.detail, name='detail'),
    path('new/', views.new, name="new"),
    path('items/<int:pk>/delete/', views.delete, name='delete'),
    path('items/<int:pk>/edit/', views.edit, name='edit'),
]