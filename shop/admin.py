from django.contrib import admin
from . models import product,Contact,Checkout
# Register your models here.
admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Checkout)

