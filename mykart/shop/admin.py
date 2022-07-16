from django.contrib import admin

from .models import Product, Contact, Order, OrderUpdate

class productAdmin(admin.ModelAdmin):
    list_display = ('prod_name','price' ,'category','pub_date')
class contactAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone')

class TrackAdmin(admin.ModelAdmin):
    list_display = ('update_desc','order_id','timestamp')

admin.site.register(Product, productAdmin)
admin.site.register(Contact,contactAdmin)
admin.site.register(Order,contactAdmin)
admin.site.register(OrderUpdate,TrackAdmin)


