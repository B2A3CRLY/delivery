from django.contrib import admin
from .models import Client, Parcel, Article, Delivery, ParcelQuantity

admin.site.register(Client)
admin.site.register(Parcel)
admin.site.register(Article)
admin.site.register(Delivery)
admin.site.register(ParcelQuantity)
