from django.contrib import admin
from .models import EntrustApplication

@admin.register(EntrustApplication)
class EntrustApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'pet_name', 'status', 'application_time')
    list_filter = ('status', 'application_time')
    search_fields = ('name', 'pet_name')
