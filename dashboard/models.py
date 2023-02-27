from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from datetime import date, timedelta, timezone
class Plan(models.Model):
    name = models.CharField(max_length=255)
    messages_limit = models.CharField(max_length=255,null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField(blank=True, null=True)  # duration in days

    def __str__(self):
        return self.name

class Subscription(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.plan.name}'
    
    def save(self, *args, **kwargs):
        if not self.pk:  # subscription is being created
            self.start_date = date.today()
            self.end_date = self.start_date + timedelta(days=self.plan.duration)
        super().save(*args, **kwargs)
        
        

class newdata(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    Isim = models.CharField(max_length=255, blank=True, null=True)
    Soyisim = models.CharField(max_length=255, blank=True, null=True)
    SmsIzin = models.BooleanField(blank=True, null=True)
    CepTelefonu = models.CharField(max_length=255, blank=True, null=True)
    UyeID = models.IntegerField(primary_key=True,default=0)
    products_1 = models.CharField(max_length=255, blank=True, null=True)
    products_2 = models.CharField(max_length=255, blank=True, null=True)
    products_3 = models.CharField(max_length=255, blank=True, null=True)
    products_4 = models.CharField(max_length=255, blank=True, null=True)
    products_5 = models.CharField(max_length=255, blank=True, null=True)
    products_6 = models.CharField(max_length=255, blank=True, null=True)
    products_7 = models.CharField(max_length=255, blank=True, null=True)
    products_8 = models.CharField(max_length=255, blank=True, null=True)
    products_9 = models.CharField(max_length=255, blank=True, null=True)
    products_10 = models.CharField(max_length=255, blank=True, null=True)
    products_11 = models.CharField(max_length=255, blank=True, null=True)
    products_12 = models.CharField(max_length=255, blank=True, null=True)
    products_13 = models.CharField(max_length=255, blank=True, null=True)
    products_14 = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.UyeID)
    
class fetch_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website_link = models.CharField(max_length=255, blank=True, null=True,default='http://karumrouge.com/')
    uni_code = models.CharField(max_length=255, blank=True, null=True,default='<tem:UyeKodu>1MAG6YAT4FFLA1FG5Y1UJFQE10JK6T</tem:UyeKodu>')
    def __str__(self):
        return self.website_link