from django.contrib import admin
from django.apps import apps

# Get a list of all models in the app
app_models = apps.get_app_config("app").get_models()

# Register all models in the admin site
for model in app_models:
    admin.site.register(model)
