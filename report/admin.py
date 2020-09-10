from django.contrib import admin
from .models import Product, ProductDetail
# Register your models here.
# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','id')
    fields =  ['product_name',]
@admin.register(ProductDetail)
class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ('id','product','year','sales')
    fields = ['product','year','sales']
