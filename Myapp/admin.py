from django.contrib import admin
from .models import cars
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(cars)

class cars_data(ImportExportModelAdmin):
    pass

