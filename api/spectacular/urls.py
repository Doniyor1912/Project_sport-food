from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView




urlpatterns = [
    path('',
         SpectacularSwaggerView.as_view(
             url_name='schema'), name='swagger-ui'),
]