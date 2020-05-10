from django.urls import path

from .views import karya_akhir_placeholder_views, read_surat_karya_akhir

urlpatterns = [
    path('', karya_akhir_placeholder_views, name='karya_akhir_placeholder_views'),
    path('surat/', read_surat_karya_akhir, name='read_surat_karya_akhir'),
]
