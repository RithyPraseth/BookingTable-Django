from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.
admin.site.site_header = "Booking Table Restaurant"
admin.site.site_title = "Booking Table Restaurant Admin Panel"
admin.site.index_title = "Booking Table Restaurant Admin Panel"


class ProductAdmin(admin.ModelAdmin):
    list_display = ["foodName","image_preview","categoryID","foodDate"]
    list_filter = ["foodDate"]
    search_fields = ["foodName"]
    date_hierarchy = "foodDate"
    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        if obj.foodImage:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.foodImage.url)
        return "No Image"

    image_preview.short_description = 'Image Preview'

class CatalogAdmin(admin.ModelAdmin):
    list_display = ["catalogName","image_preview","catalogDate"]
    list_filter = ["catalogDate"]
    search_fields = ["catalogName"]
    date_hierarchy = "catalogDate"
    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        if obj.catalogImage:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.catalogImage.url)
        return "No Image"

    image_preview.short_description = 'Image Preview'

admin.site.register(Category)
admin.site.register(tblFoodMenu, ProductAdmin)
admin.site.register(tblTopMenu)
admin.site.register(tblSub2TopMenu)
admin.site.register(tblSubTopMenu)
admin.site.register(tblAboutUs)
admin.site.register(tblEnventCatalog, CatalogAdmin)