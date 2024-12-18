from rest_framework import serializers
from .models import Product,Interaction

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','description','price','category']

class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Interaction
        fields=['id','user','product','action','timestamp']
        
