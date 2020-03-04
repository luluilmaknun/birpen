from django.urls import path

from .views import pengumuman_placeholder_views, login, edit_pengumuman, \
    get_pengumuman_default, filter_pengumuman


urlpatterns = [
    path('', pengumuman_placeholder_views, name='pengumuman_placeholder_views'),
    path('login', login, name='pengumuman_login'),
    path('get-pengumuman', get_pengumuman_default, name='get_pengumuman'),
    path('filter-pengumuman', filter_pengumuman, name='filter_pengumuman'),
    path('<str:key>/edit/', edit_pengumuman, name='edit_pengumuman'),
]
