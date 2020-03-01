from django.urls import path

from .views import pengumuman_placeholder_views, login, login_form


urlpatterns = [
    path('', pengumuman_placeholder_views, name='pengumuman_placeholder_views'),
    path('login', login, name='pengumuman_login'),
    path('login-form', login_form, name='login'),
]
