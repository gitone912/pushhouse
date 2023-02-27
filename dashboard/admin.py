
# Register your models here.
from django.contrib import admin
from .models import Plan, Subscription,newdata,fetch_data

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','messages_limit', 'duration')

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
    
class newdataAdmin(admin.ModelAdmin):
    list_display = ('Isim', 'Soyisim', 'SmsIzin', 'CepTelefonu', 'UyeID', 'created_at', 'updated_at')

admin.site.register(newdata, newdataAdmin)

class fetch_dataAdmin(admin.ModelAdmin):
    list_display = ('user', 'website_link')
admin.site.register(fetch_data, fetch_dataAdmin)