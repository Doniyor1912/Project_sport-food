from django.shortcuts import render
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import mixins
from rest_framework.permissions import *
from rest_framework.viewsets import GenericViewSet

from FAQ.models import FaqModel
from FAQ.permission import ReadOnly
from FAQ.serializers import FAqSerializers

@extend_schema_view(
    list=extend_schema(summary='List Faq', tags=['FAQ']),
    retrieve=extend_schema(summary='Retrieve Faq', tags=['FAQ']),
    create=extend_schema(summary='Create Faq', tags=['FAQ']),
    update=extend_schema(summary='Update Faq', tags=['FAQ']),
    partial_update=extend_schema(summary='Partial_update Faq', tags=['FAQ']),
    destroy=extend_schema(summary='Destroy Faq', tags=['FAQ'])
)
class FaqAdminViews(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = FaqModel.objects.all()
    serializer_class = FAqSerializers
    permission_classes = (IsAdminUser,ReadOnly)


