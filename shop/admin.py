from django.contrib import admin
from .models import Products, Order
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    def change_category_to_defaul(self, request, queryset):
        queryset.update(category="default")

    change_category_to_defaul.short_description = "Default Category"

    list_display = ("title", "price", "discount_price",
                    "category")
    search_fields = ("title",)
    actions = ("change_category_to_defaul",)
    # fields = ("title", "price",)
    list_editable = ("price", "category", "discount_price")


admin.site.register(Products, ProductAdmin)
admin.site.register(Order)
