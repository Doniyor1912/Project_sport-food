from django.urls import path, include
from rest_framework import routers

from product.views import *

router = routers.SimpleRouter()
router.register(r'upload-image', CUpdateimage, basename='uploadimage')



urlpatterns = [
    #Products
    path('product/getlist-product/', CRUDProducts.as_view({'get': 'list'})),
    path('product/get-product/<int:pk>/', CRUDProducts.as_view({'get': 'retrieve'})),

    #Category
    path('product/create-category/', CRUDCategory.as_view({'post': 'create'})),
    path('product/getlist-category/', CRUDCategory.as_view({'get': 'list'})),
    path('product/put-category/<int:pk>/', CRUDCategory.as_view({'put': 'update'})),
    path('product/patch-category/<int:pk>/', CRUDCategory.as_view({'patch': 'partial_update'})),
    path('product/delete-category/<int:pk>/', CRUDCategory.as_view({'delete': 'destroy'})),
    path('product/get-category/<int:pk>/', CRUDCategory.as_view({'get': 'retrieve'})),

    # Products Details
    path('product/create-productdetails/', CRUDProductsDetails.as_view({'post': 'create'})),
    path('product/getlist-productdetails/', CRUDProductsDetails.as_view({'get': 'list'})),
    path('product/put-productdetails/<int:pk>/', CRUDProductsDetails.as_view({'put': 'update'})),
    path('product/patch-productdetails/<int:pk>/', CRUDProductsDetails.as_view({'patch': 'partial_update'})),
    path('product/delete-productdetails/<int:pk>/', CRUDProductsDetails.as_view({'delete': 'destroy'})),
    path('product/get-productdetails/<int:pk>/', CRUDProductsDetails.as_view({'get': 'retrieve'})),

    # Products Testimonial
    path('product/create-testimonial/', CRUDPTestimonial.as_view({'post': 'create'})),
    path('product/getlist-testimonial/', CRUDPTestimonial.as_view({'get': 'list'})),
    path('product/put-testimonial/<int:pk>/', CRUDPTestimonial.as_view({'put': 'update'})),
    path('product/patch-testimonial/<int:pk>/', CRUDPTestimonial.as_view({'patch': 'partial_update'})),
    path('product/delete-testimonial/<int:pk>/', CRUDPTestimonial.as_view({'delete': 'destroy'})),
    path('product/get-testimonial/<int:pk>/', CRUDPTestimonial.as_view({'get': 'retrieve'})),

    # Total products
    path('product/getlist-total/', ProductsList.as_view({'get': 'list'})),
    # Upload image
    path('', include(router.urls))
]