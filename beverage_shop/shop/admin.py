from django.contrib import admin
from .models import Category, Product, Customer, Order

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'product',
        'quantity',
        'total_amount',
        'status',
        'created_at'
    )

    list_filter = ('status',)