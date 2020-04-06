"""SSO UI admin module."""
from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from .models import Profile

app = apps.get_app_config('sso_ui')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin class."""

    def has_change_permission(self, request, obj=None):
        """Prevent admin from modifying user profile."""
        return False

for model_name, model in app.models.items():
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        continue
