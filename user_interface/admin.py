from django.contrib import admin
from user_interface.models import Type, Unit, BaseUnit

class TypeAdmin(admin.ModelAdmin):
    pass

class UnitAdmin(admin.ModelAdmin):
    pass

class BaseUnitAdmin(admin.ModelAdmin):
    pass

admin.site.register(Type, TypeAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(BaseUnit, BaseUnitAdmin)

# Register your models here.
