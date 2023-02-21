from django.contrib.auth.models import User
from django.db import models

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255 , blank=True , null=True)
    company = models.CharField(max_length=255 , blank=True , null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    company_site = models.URLField(blank=True, null=True)
    country = models.CharField(max_length=255 , blank=True , null=True)
    communication = models.CharField(max_length=255, blank=True, null=True)
    client_id = models.CharField(max_length=255, primary_key=True)
    client_secret = models.CharField(max_length=255 , blank=True , null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    structure = models.CharField(max_length=255 , blank=True , null=True)
    auth_code = models.CharField(max_length=255, blank=True, null=True)
    allow_changes = models.BooleanField()

    def __str__(self):
        return self.full_name
