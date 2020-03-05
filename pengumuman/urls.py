from django.urls import path

from .views import pengumuman_placeholder_views, login, edit_pengumuman, dropdown_pengumuman, \
    filter_pengumuman, delete_pengumuman, read_pengumuman, create_pengumuman


urlpatterns = [
    path('', pengumuman_placeholder_views, name='pengumuman_placeholder_views'),
    path('login', login, name='pengumuman_login'),
    path('filter-pengumuman', filter_pengumuman, name='filter_pengumuman'),
    path('<str:key>/edit/', edit_pengumuman, name='edit_pengumuman'),
    path('create/', create_pengumuman, name='create_pengumuman'),
    path('dropdown/', dropdown_pengumuman, name='dropdown_pengumuman'),
    path('<str:key>/delete/', delete_pengumuman, name='delete_pengumuman'),
    path('<str:key>/', read_pengumuman, name='read_pengumuman'),
]
