from django.contrib import admin
from Farmer.models import FarmerData,FarmData,ScheduleData

class FarmerDataAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone_number','language',)
class FarmDataAdmin(admin.ModelAdmin):
    list_display = ('id','farmer','area','village','crop_grown','sowing_date',)
class ScheduleDataAdmin(admin.ModelAdmin):
    list_display = ('id','farmer','farmer_farm','days_after_sowing','fertilizer','quantity','quantity_unit',)

admin.site.register(FarmerData, FarmerDataAdmin)
admin.site.register(FarmData, FarmDataAdmin)
admin.site.register(ScheduleData, ScheduleDataAdmin)
