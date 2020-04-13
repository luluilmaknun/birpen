from django.urls import path
from .views import read_all_admin


urlpatterns = [
    path('', read_all_admin, name='read_all_asdos'),
]
