from django.urls import path
from .views import permohonan_surat_placeholder_views, create_pesanan_surat_akademik


urlpatterns = [
    path('', permohonan_surat_placeholder_views, name='permohonan_surat_placeholder_views'),
    path('pesanan/create/', create_pesanan_surat_akademik,
         name='create_pesanan_surat_akademik'),
]
