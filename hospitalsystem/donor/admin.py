from django.contrib import admin
from .models import Donor, BloodDonate

class DonorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Donor,DonorAdmin)

class BloodDonateAdmin(admin.ModelAdmin):
    pass
admin.site.register(BloodDonate,BloodDonateAdmin)

 