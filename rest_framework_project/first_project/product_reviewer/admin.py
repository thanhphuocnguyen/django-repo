from django.contrib import admin
from .models import Cateogry, Comment, Company, Image, Product, ProductSite, ProductSize
from django.contrib.auth.models import Group
from django.contrib import admin

# Register your models here.
admin.site.register(Cateogry)
admin.site.register(Company)
admin.site.register(Comment)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'content')
    list_filter = ('category', )


admin.site.register(ProductSite)
admin.site.register(ProductSize)
admin.site.unregister(Group)
admin.site.register(Image)