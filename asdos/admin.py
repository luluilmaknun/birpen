from django.apps import apps
from django.contrib import admin

app = apps.get_app_config('asdos')

class DisplayUsername(admin.ModelAdmin):
    list_display = ['username']

for model_name, model in app.models.items():
    admin.site.register(model, DisplayUsername)
