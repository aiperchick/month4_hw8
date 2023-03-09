from django.contrib import admin
from . import models

admin.site.register(models.CustomerCl)
admin.site.register(models.OrderCl)
admin.site.register(models.ProductCl)
admin.site.register(models.TagCl)
