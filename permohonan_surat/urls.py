from django.urls import path
from .views import permohonan_surat_placeholder_views, create_pesanan_surat_akademik, \
    get_mahasiswa_profile, read_surat_akademik


urlpatterns = [
    path('', permohonan_surat_placeholder_views, name='permohonan_surat_placeholder_views'),
    path('pesanan/create/', create_pesanan_surat_akademik,
         name='create_pesanan_surat_akademik'),
    path('pesanan/mahasiswa-profile/', get_mahasiswa_profile, name='get_mahasiswa_profile'),
    path('surat-akademik/', read_surat_akademik, name='read_surat_akademik'),
]
