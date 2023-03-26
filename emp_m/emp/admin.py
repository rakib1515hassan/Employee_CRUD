from django.contrib import admin
from .models import Employee_Info

# Register your models here.
class Employee_Info_Admin(admin.ModelAdmin):
    list_display =(
        'full_name','gender','email','phone','image','position','address',
    )
admin.site.register(Employee_Info)
