from django.urls import path
from .views import alumni_placeholder_views


urlpatterns = [
    path('', alumni_placeholder_views, name='alumni_placeholder_views'),
]
