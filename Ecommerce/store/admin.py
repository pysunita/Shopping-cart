from django.contrib import admin
from.models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user','name','email']
admin.site.register(Customer,CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','image']
admin.site.register(Product,ProductAdmin)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer','date_ordered','transaction_id']
admin.site.register(Order,OrderAdmin)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product','order','quantity', 'date_added']
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(ShippingAddress)
