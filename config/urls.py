from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]


urlpatterns += i18n_patterns(
    path("i18n/", include('django.conf.urls.i18n')),

    path('api/', include('api.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),

)


