from django.urls import path

from .views import karya_akhir_placeholder_views, edit_data_karya_akhir

urlpatterns = [
    path('', karya_akhir_placeholder_views, name='karya_akhir_placeholder_views'),
    path('edit/', edit_data_karya_akhir, name='edit_data_karya_akhir'),
]
