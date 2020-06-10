from django.urls import path

from .views import pengumuman_placeholder_views, edit_pengumuman, dropdown_pengumuman, \
    filter_pengumuman, delete_pengumuman, read_pengumuman_by_pk, create_pengumuman, \
    get_pengumuman_default

urlpatterns = [
    path('', pengumuman_placeholder_views, name='pengumuman_placeholder_views'),
    path('get-pengumuman', get_pengumuman_default, name='get_pengumuman'),
    path('filter-pengumuman', filter_pengumuman, name='filter_pengumuman'),
    path('<str:key>/edit/', edit_pengumuman, name='edit_pengumuman'),
    path('create/', create_pengumuman, name='create_pengumuman'),
    path('dropdown/', dropdown_pengumuman, name='dropdown_pengumuman'),
    path('<str:key>/delete/', delete_pengumuman, name='delete_pengumuman'),
    path('<str:key>/', read_pengumuman_by_pk, name='read_pengumuman_by_pk'),
]
