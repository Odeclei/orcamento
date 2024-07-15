from django.contrib import admin

from acompany import models

# Register your models here.


@admin.register(models.enterprise)
class enterpriseAdmin(admin.ModelAdmin):
    list_display = 'fantasyName', 'cnpj', 'phone', 'contact',
    ordering = 'name',
    search_fields = ("name", "cnpj", "contact",)
    list_filter = ("created_at", "city",)
    list_per_page = 50
