from django.contrib import admin
from . models import Category, Service
# # Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=['category_name','slug']
    prepopulated_fields = {'slug':('category_name',)}
admin.site.register(Category,CategoryAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_category','service_name','service_price']
    prepopulated_fields = {'slug':('service_name',)}
admin.site.register(Service,ServiceAdmin)