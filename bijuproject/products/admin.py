from django.contrib import admin
from . import models

admin.site.register(models.Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'availability', 'image', 'description', 'composition')
