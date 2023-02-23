
# Register your models here.
from django.contrib import admin
from .models import Plan, Subscription

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user','user_full_name', 'user_email', 'plan', 'start_date', 'end_date')
    list_filter = ('plan', 'start_date', 'end_date')
    search_fields = ('user__username', 'plan__name')

    def user_full_name(self, obj):
        return obj.user.get_full_name()
    user_full_name.short_description = 'User Full Name'

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'Email'