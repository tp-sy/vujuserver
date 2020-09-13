from django.contrib import admin
from .models import Product, Song, UserInfo

admin.site.register(Product)
admin.site.register(Song)
admin.site.register(UserInfo)
