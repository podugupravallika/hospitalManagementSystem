from django.contrib import admin
from .models import Patientt

class BloodPatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patientt,BloodPatientAdmin)
