from django.urls import path
from .views import alumni_placeholder_views, register


urlpatterns = [
    path('', alumni_placeholder_views, name='alumni_placeholder_views'),
    path('register/', register, name='register'),
]
