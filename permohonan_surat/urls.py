from django.urls import path
from .views import permohonan_surat_placeholder_views, read_status_bayar


urlpatterns = [
    path('', permohonan_surat_placeholder_views, name='permohonan_surat_placeholder_views'),
    path('status-bayar/', read_status_bayar, name='read_status_bayar')
]
