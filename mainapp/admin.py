from django.contrib import admin

from mainapp.models import ProductCategory, Product

#admin.site.register(Product)
admin.site.register(ProductCategory)

#@admin.register(Product)
#class ProductAdmin(admin.ModelAdmin):
#   list_display = ('name', 'price', 'quantity', 'category')
#    fields = ('name', 'image', 'short_description', ('price', 'quantity'), 'category')
#    во вложенном кортэре указыватся поля, которые необходимо отобразить в одну строчку
#    ordering = ('name')
#   search_fields = ('name')