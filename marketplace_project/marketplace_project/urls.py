from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('marketplace_app.urls')),
    path('', include('item.urls')),
    path('', include('dashboard.urls')),
]
