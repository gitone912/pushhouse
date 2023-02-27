from rest_framework import serializers
from .models import *

class userdataform(serializers.ModelSerializer):
    class Meta:
        model = newdata
        exclude = ('created_at', 'updated_at')