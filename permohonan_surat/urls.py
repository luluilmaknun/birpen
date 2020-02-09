from django.urls import path
from .views import permohonan_surat_placeholder_views


urlpatterns = [
    path('', permohonan_surat_placeholder_views, name='permohonan_surat_placeholder_views'),
]
