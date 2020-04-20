from django.urls import path
from .views import alumni_placeholder_views, register, update_block_status


urlpatterns = [
    path('', alumni_placeholder_views, name='alumni_placeholder_views'),
    path('register/', register, name='register'),
    path('<username>/block/', update_block_status, name='update_block_status'),
]
