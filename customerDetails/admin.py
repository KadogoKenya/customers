from django.contrib import admin
from . models import LocationDetails,Business

# Register your models here.
class BusinessAdmin(admin.ModelAdmin):
    pass
admin.site.register(Business,BusinessAdmin)

class LocationAdmin(admin.ModelAdmin):
    pass
admin.site.register(LocationDetails,LocationAdmin)
