from django.contrib.auth.models import User
from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.openapi import AutoSchema
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import mixins, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Updateimage
from .serializers import *


class ProductsPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000

@extend_schema_view(
    list=extend_schema(summary='List product', tags=['Products']),
    retrieve=extend_schema(summary='Retrieve product', tags=['Products']))
class CRUDProducts(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    serializer_class = ProductsSerializers
    pagination_class = ProductsPagination
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
    )
    search_fields = ['name']



    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Products.objects.all()

        return Products.objects.filter(pk=pk)


@extend_schema_view(
    list=extend_schema(summary='List Category', tags=['Category']),
    retrieve=extend_schema(summary='Retrieve Category', tags=['Category']),
    create=extend_schema(summary='Create Category', tags=['Category']),
    update=extend_schema(summary='Update Category', tags=['Category']),
    partial_update=extend_schema(summary='Partial_update Category', tags=['Category']),
    destroy=extend_schema(summary='Destroy Category', tags=['Category'])
)
class CRUDCategory(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = CategorySerializers
    filter_backends = [SearchFilter]
    pagination_class = ProductsPagination
    search_fields = ['name']



    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Category.objects.all()

        return Category.objects.filter(pk=pk)


@extend_schema_view(
    list=extend_schema(summary='List product Details', tags=['Products details']),
    retrieve=extend_schema(summary='Retrieve product Details', tags=['Products details']),
    create=extend_schema(summary='Create product Details', tags=['Products details']),
    update=extend_schema(summary='Update product Details', tags=['Products details']),
    partial_update=extend_schema(summary='Partial_update product Details', tags=['Products details']),
    destroy=extend_schema(summary='Destroy product Details', tags=['Products details']
))
class CRUDProductsDetails(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = ProductsDetailsSerializers
    filter_backends = [SearchFilter]
    pagination_class = ProductsPagination
    search_fields = ['name']


    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Products.objects.all()

        return Products.objects.filter(pk=pk)




@extend_schema_view(
    list=extend_schema(summary='List product ', tags=['Testimonial']),
    retrieve=extend_schema(summary='Retrieve product ', tags=['Testimonial']),
    create=extend_schema(summary='Create product ', tags=['Testimonial']),
    update=extend_schema(summary='Update product ', tags=['Testimonial']),
    partial_update=extend_schema(summary='Partial_update product ', tags=['Testimonial']),
    destroy=extend_schema(summary='Destroy product ', tags=['Testimonial']
))
class CRUDPTestimonial(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = TestimonialSerializers
    pagination_class = ProductsPagination
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
    )
    search_fields = ['customer_name']



    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Testimonial.objects.all()

        return Testimonial.objects.filter(pk=pk)

@extend_schema_view(
    list=extend_schema(summary='List product total', tags=['Total products']),
)
class ProductsList(mixins.ListModelMixin,GenericViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            "total_products": self.get_queryset().count(),
            "total_categories": Category.objects.count(),
            "total_users": User.objects.count(),
        }
        return Response(response.data)

@extend_schema_view(
    create=extend_schema(summary='Create image', tags=['Update Image']),
)
class CUpdateimage(mixins.CreateModelMixin,
                   GenericViewSet):
    serializer_class = UpdateimageSerializers
    queryset = Updateimage.objects.all()
