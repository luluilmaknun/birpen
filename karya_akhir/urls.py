from django.urls import path

from .views import karya_akhir_placeholder_views, read_program_studi

urlpatterns = [
    path('', karya_akhir_placeholder_views, name='karya_akhir_placeholder_views'),
    path('program-studi/', read_program_studi, name='read_program_studi'),
]
