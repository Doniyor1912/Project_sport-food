from django.db import router
from django.urls import include, path
from rest_framework import routers

from api.spectacular.urls import urlpatterns as doc_urls
from users.urls import urlpatterns as users_urls


urlpatterns = [
]


urlpatterns += doc_urls
urlpatterns += users_urls