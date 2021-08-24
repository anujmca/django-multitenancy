from django.contrib import admin
from sweet_tenant.models import Sweet
# Register your models here.


@admin.register(Sweet)
class SweetAdmin(admin.ModelAdmin):
    list_display= ['name']

