from django.urls import path
from .views import read_all_asdos, create_asisten, delete_asdos


urlpatterns = [
    path('', read_all_asdos, name='read_all_asdos'),
    path('create-asisten/', create_asisten, name='create-asisten'),
    path('<str:username>/delete/', delete_asdos, name='delete_asdos'),
]
