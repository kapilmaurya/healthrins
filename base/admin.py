from django.contrib import admin

from base.models import Address, Order_items, Product, Profile,Cart,Order_details

# Register your models here.
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(Order_items)
admin.site.register(Order_details)



