from django.contrib import admin
from tenant.models import Tenant, TenantDecision, Apartments, Location, RentPerMonth

class TenantAdmin(admin.ModelAdmin):
    List_display = ['Class_Name', 'Class_Teacher_Name', ]
admin.site.register(Tenant, TenantAdmin)

class TenantDecisionAdmin(admin.ModelAdmin):
    List_display = ['Class_Name', 'Class_Teacher_Name', ]
admin.site.register(TenantDecision, TenantDecisionAdmin)

class ApartmentsAdmin(admin.ModelAdmin):
    List_display = ['Class_Name', 'Class_Teacher_Name', ]
admin.site.register(Apartments, ApartmentsAdmin)

class LocationAdmin(admin.ModelAdmin):
    List_display = ['Class_Name', 'Class_Teacher_Name', ]
admin.site.register(Location, LocationAdmin)

class RentPerMonthAdmin(admin.ModelAdmin):
    List_display = ['Class_Name', 'Class_Teacher_Name', ]
admin.site.register(RentPerMonth, RentPerMonthAdmin)


# Register your models here.
