from django.contrib import admin
from .models import Collection, Care, Item

# Register your models here.
admin.site.register(Collection)
admin.site.register(Care)
admin.site.register(Item)