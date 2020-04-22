"""SSO UI urls module."""
from django.urls import path
from django_cas_ng import views as cas_views

from .views import save_user_info, obtain_user_info, refresh_data

app_name = 'sso_ui'
urlpatterns = [
    path('login/', cas_views.LoginView.as_view(), name='login'),
    path('logout/', cas_views.LogoutView.as_view(), name='logout'),
    path('save_user_info/', save_user_info, name='save_user_info'),
    path('obtain-user-info/', obtain_user_info, name='obtain_user_info'),
    path('refresh-data/', refresh_data, name='refresh_data'),
]
