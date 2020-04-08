from django.urls import path
from .views import asdos_placeholder_views, create_asisten, delete_asdos


urlpatterns = [
    path('', asdos_placeholder_views, name='asdos_placeholder_views'),
    path('create-asisten/', create_asisten, name='create-asisten'),
    path('delete/', delete_asdos, name='delete_asdos'),
]
