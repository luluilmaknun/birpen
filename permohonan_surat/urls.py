from django.urls import path

from .views import permohonan_surat_placeholder_views, create_pesanan_surat_akademik,\
    get_status_surat

urlpatterns = [
    path('', permohonan_surat_placeholder_views, name='permohonan_surat_placeholder_views'),
    path('pesanan/create/', create_pesanan_surat_akademik,
         name='create_pesanan_surat_akademik'),
    path('status-surat/get/', get_status_surat, name='get_status_surat'),
]
