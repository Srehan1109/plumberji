from django.contrib import admin
from .models import Account, PlumberProfile
# Register your models here.
admin.site.register(Account)

class plumberProfileAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','username','email','phone_number']
admin.site.register(PlumberProfile)

# class RoleAdmin(admin.ModelAdmin):
#     list_display=['role_name']
# admin.site.register(Role,RoleAdmin)
