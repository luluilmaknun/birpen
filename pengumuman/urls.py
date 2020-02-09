from django.urls import path
from .views import pengumuman_placeholder_views


urlpatterns = [
    path('', pengumuman_placeholder_views, name='pengumuman_placeholder_views'),
]
