from django.contrib import admin
from .models import Customer , Supplier ,Order ,ManageStore # استورد الموديل بتاعك

# سجل الموديل عشان يظهر في لوحة التحكم
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Order)
admin.site.register(ManageStore)