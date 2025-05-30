from django.contrib import admin
from .models import Pet, CorporatePet, AdoptionApplication

admin.site.register(Pet)
admin.site.register(CorporatePet)
admin.site.register(AdoptionApplication)
