from django.contrib import admin
from products.models import ProductCategory, Product, Basket



@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description',('price', 'quantity'), 'image', 'category')
    search_fields = ('name',)
    ordering = ('name', )


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity',)
    readonly_fields = ('created_timestamp',)
    extra = 0
