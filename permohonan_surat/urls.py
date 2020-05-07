from django.urls import path

from .views import permohonan_surat_placeholder_views, create_pesanan_surat_akademik, \
    read_pesanan, read_pesanan_detail, update_status_surat, update_status_bayar, \
    read_status_bayar, get_status_surat, get_mahasiswa_profile, read_surat_akademik


urlpatterns = [
    path('', permohonan_surat_placeholder_views, name='permohonan_surat_placeholder_views'),
    path('status-bayar/', read_status_bayar, name='read_status_bayar'),
    path('status-surat/', get_status_surat, name='get_status_surat'),
    path('surat-akademik/', read_surat_akademik, name='read_surat_akademik'),
    path('pesanan/create/', create_pesanan_surat_akademik,
         name='create_pesanan_surat_akademik'),
    path('pesanan/mahasiswa-profile/', get_mahasiswa_profile, name='get_mahasiswa_profile'),
    path('pesanan/', read_pesanan, name='read_pesanan'),
    path('pesanan/<id_pesanan>/', read_pesanan_detail, name='read_pesanan_detail'),
    path(
        'pesanan/<id_pesanan>/surat-akademik/<jenis_dokumen>/update-status/',
        update_status_surat, name='update_status_surat',
    ),
    path('pesanan/<id_pesanan>/update-status-bayar/', update_status_bayar,
         name='update_status_bayar'),
]
