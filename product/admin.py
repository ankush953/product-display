from django.contrib import admin

#import apps from models
from product.models import Product, Review

# Register your models here.
admin.site.register(Product)
admin.site.register(Review)


