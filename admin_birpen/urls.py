from django.urls import path

from .views import read_all_admin, create_admin, delete_admin

urlpatterns = [
    path('', read_all_admin, name='read_all_admin'),
    path('create/', create_admin, name='create_admin'),
    path('<str:username>/delete/', delete_admin, name='delete_admin'),
]
