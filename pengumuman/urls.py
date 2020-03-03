from django.urls import path

from .views import pengumuman_placeholder_views, login, get_pengumuman_default

urlpatterns = [
    path('', pengumuman_placeholder_views, name='pengumuman_placeholder_views'),
    path('login', login, name='pengumuman_login'),
    path('get-pengumuman', get_pengumuman_default, name='get_pengumuman'),
]
