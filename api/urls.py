
from api.spectacular.urls import urlpatterns as doc_urls
from users.urls import urlpatterns as users_urls
from FAQ.urls import urlpatterns as faq_urls
from product.urls import urlpatterns as product_urls
from imageproxy.urls import urlpatterns as image_urls


urlpatterns = [
]


urlpatterns += doc_urls
urlpatterns += users_urls
urlpatterns += faq_urls
urlpatterns += product_urls
urlpatterns += image_urls
