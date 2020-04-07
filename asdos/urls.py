from django.urls import path
from .views import asdos_placeholder_views, create_asisten


urlpatterns = [
    path('', asdos_placeholder_views, name='asdos_placeholder_views'),
    path('create-asisten/', create_asisten, name='create-asisten'),
]
