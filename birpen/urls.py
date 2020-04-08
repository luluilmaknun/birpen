"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView


urlpatterns = [

    # http://localhost:8000/
    path(
        '',
        include(('landing_page.urls', 'landing_page'),
                namespace='landing_page')),

    # http://localhost:8000/api/<router-viewsets>
    path(
        'api/pengumuman/',
        include(('pengumuman.urls', 'pengumuman'),
                namespace='pengumuman')),
    path(
        'api/permohonan-surat/',
        include(('permohonan_surat.urls', 'permohonan_surat'),
                namespace='permohonan_surat')),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),

    path('sso/', include('sso_ui.urls')),

    re_path(r'^.*/$', TemplateView.as_view(template_name="index.html")),

]
