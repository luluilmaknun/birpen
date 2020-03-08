"""SSO UI urls module."""
from django.urls import path
from django_cas_ng import views as cas_views

app_name = 'sso_ui'
urlpatterns = [
    path('login/', cas_views.LoginView.as_view(), name='login'),
    path('logout/', cas_views.LogoutView.as_view(), name='logout'),
]
