from django.contrib import admin

from .forms import PlumberProfileFrom
from .models import Account, PlumberProfile, Role
# # Register your models here.
admin.site.register(Account)

class plumberProfileAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','username','email','phone_number']
admin.site.register(PlumberProfile)

class RoleAdmin(admin.ModelAdmin):
    list_display=['role']
admin.site.register(Role)
