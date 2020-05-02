from django.urls import path
from .views import permohonan_surat_placeholder_views, update_status_bayar


urlpatterns = [
    path('', permohonan_surat_placeholder_views, name='permohonan_surat_placeholder_views'),
    path('pesanan/<id_pesanan>/update-status-bayar/', update_status_bayar,
         name='update_status_bayar')
]
