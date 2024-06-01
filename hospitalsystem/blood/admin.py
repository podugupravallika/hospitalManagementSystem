from django.contrib import admin
from .models import Stock,BloodRequest

class BloodAdmin(admin.ModelAdmin):
    pass
admin.site.register(BloodRequest,BloodAdmin)

class StockAdmin(admin.ModelAdmin):
    pass
admin.site.register(Stock,StockAdmin)
