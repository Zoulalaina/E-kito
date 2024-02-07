from django.contrib import admin
from store.models import Produit, Order, Cart
# Register your models here.
admin.site.register(Produit)
admin.site.register(Order)
admin.site.register(Cart)
