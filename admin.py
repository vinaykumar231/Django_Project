from django.contrib import admin

# Register your models here.
from .models import SEO
from import_export.admin import ImportExportActionModelAdmin
admin.site.register(SEO, ImportExportActionModelAdmin)