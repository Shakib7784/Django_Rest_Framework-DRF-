from django.contrib import admin
from firstapp.models import Product,ProductReview

# Register your models here.
@admin.register(Product)
class ProductListregister(admin.ModelAdmin):
    list_display=["name","description","price"]
    
    
@admin.register(ProductReview)
class ProductReviewListregister(admin.ModelAdmin):
    list_display=["user","product","rating","review","created_at","updated_at"]