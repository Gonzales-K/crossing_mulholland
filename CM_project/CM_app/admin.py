from django.contrib import admin
from .models import Collection, Care, Item, Cart, CartItem

# Register your models here.
admin.site.register(Collection)
admin.site.register(Care)
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(CartItem)