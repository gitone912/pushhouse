from django.contrib import admin
from .models import UserData

class UserDataAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'company', 'contact_phone', 'country', 'communication')
    search_fields = ('full_name', 'company', 'contact_phone', 'country', 'communication')

admin.site.register(UserData, UserDataAdmin)
