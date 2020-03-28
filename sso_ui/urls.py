"""SSO UI urls module."""
from django.urls import path
from django_cas_ng import views as cas_views

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views import create_token

app_name = 'sso_ui'
urlpatterns = [
    path('login/', cas_views.LoginView.as_view(), name='login'),
    path('logout/', cas_views.LogoutView.as_view(), name='logout'),
    path('create-token/', create_token, name='create-token'),
    path('obtain-token/', obtain_jwt_token, name='obtain_token'),
    path('refresh-token/', refresh_jwt_token, name='refresh_token')
]
