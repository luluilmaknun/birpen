from django.urls import path

from .views import karya_akhir_placeholder_views, read_data_karya_akhir_by_username, \
    read_surat_karya_akhir, read_program_studi, create_data_karya_akhir, \
    filter_mahasiswa, read_mahasiswa_karya_akhir, get_mahasiswa_profile, \
    read_jenis_karya_akhir, edit_data_karya_akhir

urlpatterns = [
    path('', karya_akhir_placeholder_views, name='karya_akhir_placeholder_views'),
    path('create/', create_data_karya_akhir, name='create_data_karya_akhir'),
    path('edit/', edit_data_karya_akhir, name='edit_data_karya_akhir'),
    path('surat/', read_surat_karya_akhir, name='read_surat_karya_akhir'),
    path('program-studi/', read_program_studi, name='read_program_studi'),
    path('mahasiswa/', read_mahasiswa_karya_akhir, name='read_mahasiswa_karya_akhir'),
    path('filter-mahasiswa', filter_mahasiswa, name='filter_mahasiswa'),
    path('jenis-karya-akhir/', read_jenis_karya_akhir, name='read_jenis_karya_akhir'),
    path('get-profile/', get_mahasiswa_profile, name='get_mahasiswa_profile'),
    path('<username>/', read_data_karya_akhir_by_username,
         name='read_data_karya_akhir_by_username'),
]
