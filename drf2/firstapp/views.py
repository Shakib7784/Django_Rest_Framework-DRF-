from django.shortcuts import render
from rest_framework import viewsets
from firstapp.models import Product,ProductReview
from firstapp.serializers import ProductSerializer,ProductReviewSerializer
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
# Create your views here.
from firstapp.permissions import AdminorReadonly,ReviewerOrReadonly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from firstapp.paginations import ProductPagination ,ProductLimitOffset, ProductCursor


class ProductList(viewsets.ModelViewSet):
    permission_classes=[AdminorReadonly]
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']
    pagination_class=ProductCursor
    
class ProductReviewList(viewsets.ModelViewSet):
    permission_classes=[ReviewerOrReadonly]
    queryset=ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["user__username","product","rating"]
    # filter_backends = [filters.SearchFilter]
    # search_fields = ["user__username",'review']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['user__username', 'rating']
    
    # def get_queryset(self):
    #     queryset=ProductReview.objects.all()
      
        # username = self.request.query_params.get('username') # we can call data by their name here,
        # rating = self.request.query_params.get("rating")
        # pname = self.request.query_params.get("name")
        # if username is not None:
        #     queryset = queryset.filter(user__username_icontains=username) # we have to give __name if it is connected as foreign key. user is connected with product review as foreign key. that's whey we have to give user_username. icontains is for avoiding lowercase, uppercase
        # if rating is not None : 
        #     queryset = queryset.filter(rating=rating)
        # if pname is not None : 
        #     queryset = queryset.filter(product__name=pname) # product is connected as foreign key. that's why to access product name we hvae to give product__name.
        # return queryset
