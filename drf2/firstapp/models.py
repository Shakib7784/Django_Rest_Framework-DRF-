from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30,default="product_1")
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self) -> str:
        return self.name
    
    
  
class ProductReview(models.Model):
    #one product will have multiple reviews
    product= models.ForeignKey(Product,on_delete=models.CASCADE,related_name="reviews")
    #one user will have multiple reviews 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i,i) for i in range(1,6)])
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta: 
        #one user will have multiple reviews. But one user will have only one review for one product 
        unique_together = ("product","user")
        
    def __str__(self) -> str:
        return f"{self.user.username}-{self.product.name}- Rating:{self.rating}"
    