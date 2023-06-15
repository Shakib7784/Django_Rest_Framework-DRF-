from rest_framework import serializers
from firstapp.models import Product,ProductReview

        
        
class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields="__all__"
        
        
class ProductSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True)
    class Meta: 
        model=Product
        fields="__all__"