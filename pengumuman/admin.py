from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .models import User

models = apps.get_models()
admin.site.register(User)


for model in models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
