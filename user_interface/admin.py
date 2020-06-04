from django.contrib import admin
from user_interface.models import Type

class TypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Type, TypeAdmin)

# Register your models here.
