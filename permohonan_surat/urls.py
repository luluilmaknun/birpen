from django.urls import path
from .views import permohonan_surat_placeholder_views, create_pesanan_surat_akademik, \
    read_pesanan, read_pesanan_detail


urlpatterns = [
    path('', permohonan_surat_placeholder_views, name='permohonan_surat_placeholder_views'),
    path('pesanan/create/', create_pesanan_surat_akademik,
         name='create_pesanan_surat_akademik'),
    path('pesanan/', read_pesanan, name='read_pesanan'),
    path('pesanan/<id_pesanan>/', read_pesanan_detail, name='read_pesanan_detail')
]
