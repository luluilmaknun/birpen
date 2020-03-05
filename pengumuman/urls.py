from django.urls import path

from .views import pengumuman_placeholder_views, login, edit_pengumuman, create_pengumuman


urlpatterns = [
    path('', pengumuman_placeholder_views, name='pengumuman_placeholder_views'),
    path('login', login, name='pengumuman_login'),
    path('<str:key>/edit/', edit_pengumuman, name='edit_pengumuman'),
    path('create/', create_pengumuman, name='create_pengumuman'),
]
