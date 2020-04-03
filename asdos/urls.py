from django.urls import path
from .views import asdos_placeholder_views


urlpatterns = [
    path('', asdos_placeholder_views, name='asdos_placeholder_views'),
]
