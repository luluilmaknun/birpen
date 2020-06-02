from django.urls import path

from .views import karya_akhir_placeholder_views, read_data_karya_akhir_by_username, \
    read_surat_karya_akhir, read_program_studi, filter_mahasiswa

urlpatterns = [
    path('', karya_akhir_placeholder_views, name='karya_akhir_placeholder_views'),
    path('surat/', read_surat_karya_akhir, name='read_surat_karya_akhir'),
    path('program-studi/', read_program_studi, name='read_program_studi'),
    path('filter-mahasiswa', filter_mahasiswa, name='filter_mahasiswa'),
    path('<username>/', read_data_karya_akhir_by_username,
         name='read_data_karya_akhir_by_username'),
]
