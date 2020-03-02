from django.urls import path

from .views import pengumuman_placeholder_views, login


urlpatterns = [
    path('', pengumuman_placeholder_views, name='pengumuman_placeholder_views'),
    path('login', login, name='pengumuman_login'),
]
