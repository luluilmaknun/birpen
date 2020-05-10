from django.urls import path

from .views import karya_akhir_placeholder_views

urlpatterns = [
    path('', karya_akhir_placeholder_views, name='karya_akhir_placeholder_views'),
]
