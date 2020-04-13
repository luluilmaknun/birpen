from django.urls import path

from .views import admin_placeholder_views

urlpatterns = [
    path('', admin_placeholder_views, name='admin_placeholder_views'),
]
