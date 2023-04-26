from django.contrib import admin
from .models import Phone, ContactUs
# Register your models here.


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'price']

admin.site.register(ContactUs)