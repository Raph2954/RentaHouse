from django.contrib import admin
from listproperty.models import Property, AddBeds


class propertyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Property, propertyAdmin)


class AddBedsAdmin(admin.ModelAdmin):
    pass
admin.site.register(AddBeds, AddBedsAdmin)