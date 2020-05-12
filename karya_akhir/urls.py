from django.urls import path

from .views import karya_akhir_placeholder_views, read_data_karya_akhir_by_username

urlpatterns = [
    path('', karya_akhir_placeholder_views, name='karya_akhir_placeholder_views'),
    path('<username>/', read_data_karya_akhir_by_username,
         name='read_data_karya_akhir_by_username'),
]
