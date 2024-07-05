from django.contrib import admin
from .models import Color, Type, Tag, BlogCategory, ProductCategory, StockStatus

admin.site.register(Color)
admin.site.register(Type)
admin.site.register(Tag)
admin.site.register(BlogCategory)
admin.site.register(ProductCategory)
admin.site.register(StockStatus)

