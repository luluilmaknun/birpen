from django.urls import path
from .views import asdos_placeholder_views, delete_asdos


urlpatterns = [
    path('', asdos_placeholder_views, name='asdos_placeholder_views'),
    path('<str:key>/delete/', delete_asdos, name='delete_asdos'),
]
