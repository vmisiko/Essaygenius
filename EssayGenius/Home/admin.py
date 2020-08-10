from django.contrib import admin
from . models import Orders, VueOrders, UploadFiles
# Register your models here.

@admin.register(Orders)
class OdersAdmin(admin.ModelAdmin):
    list_display = ["topic", "pages", "subject","uploads"]

@admin.register(UploadFiles)
class UploadFilesAdmin(admin.ModelAdmin):
    list_display = ["files", "main"]

@admin.register(VueOrders)
class VueOrdersAdmin(admin.ModelAdmin):
    list_display = ["deadline",
                    "Type",
                    "pages",
                    "service",
                    "fin_earl"]

