from django.contrib import admin
from django.urls import path,include
from firstapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"product",views.ProductList,basename="product")
router.register(r"product_review",views.ProductReviewList,basename="product_review")

urlpatterns = [
    path("",include(router.urls)),
    # path("api_auth",include("rest_framework.urls")),
]