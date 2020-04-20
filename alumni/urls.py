from django.urls import path
from .views import read_all_alumni, register, update_block_status


urlpatterns = [
    path('', read_all_alumni, name='read_all_alumni'),
    path('register/', register, name='register'),
    path('<username>/block/', update_block_status, name='update_block_status'),
]
