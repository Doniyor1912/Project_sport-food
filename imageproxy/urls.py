from django.urls import path
from .views import ImageProxyView

urlpatterns = [
    path('proxy-image/', ImageProxyView.as_view(), name='proxy-image'),
]