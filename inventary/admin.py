from django.contrib import admin
from .models import ProductModel,GroupProductModel,ShoppingCartModel

admin.site.register(ProductModel)
admin.site.register(GroupProductModel)
admin.site.register(ShoppingCartModel)