from django.urls import path

from .views import karya_akhir_placeholder_views, create_data_karya_akhir

urlpatterns = [
    path('', karya_akhir_placeholder_views, name='karya_akhir_placeholder_views'),
    path('create/', create_data_karya_akhir, name='create_data_karya_akhir'),
]
