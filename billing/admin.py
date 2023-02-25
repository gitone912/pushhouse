from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CreditCard
from .models import BillingAddress
@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    list_display = ('user', 'cardholder_name', 'card_type', 'card_number', 'expiration_date')
    list_filter = ('user',)
    search_fields = ('user__email', 'cardholder_name', 'card_type', 'card_number')

from django.contrib import admin
from .models import BillingAddress

@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'city', 'country', 'is_default')
    list_filter = ('is_default',)
    search_fields = ('full_name', 'city', 'country')
    ordering = ('-is_default',)
    fieldsets = (
        (None, {
            'fields': ('user', 'full_name', 'phone_number')
        }),
        ('Address', {
            'fields': ('company_name', 'address_line_1', 'address_line_2', 'city', 'state', 'postal_code', 'country')
        }),
        ('Default', {
            'fields': ('is_default',)
        }),
    )


