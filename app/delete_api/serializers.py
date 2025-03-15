from rest_framework import serializers 
from .models import Data

class ItemSerializer(serializers.ModelSerializer):
     class Meta:
          model = Data
          fields = ['name','description','id']