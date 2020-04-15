from django.urls import path

from .views import admin_placeholder_views, create_admin, delete_admin

urlpatterns = [
    path('', admin_placeholder_views, name='admin_placeholder_views'),
    path('create/', create_admin, name='create_admin'),
    path('<str:username>/delete/', delete_admin, name='delete_admin'),
]
