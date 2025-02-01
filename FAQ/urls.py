from django.urls import path

from FAQ.views import FaqAdminViews

urlpatterns = [
    # FAQ
    path('comments/admin/create-category/', FaqAdminViews.as_view({'post': 'create'})),
    path('comments/admin/getlist-category/', FaqAdminViews.as_view({'get': 'list'})),
    path('comments/admin/put-category/<int:pk>/', FaqAdminViews.as_view({'put': 'update'})),
    path('comments/admin/patch-category/<int:pk>/', FaqAdminViews.as_view({'patch': 'partial_update'})),
    path('comments/admin/delete-category/<int:pk>/', FaqAdminViews.as_view({'delete': 'destroy'})),
    path('comments/admin/get-category/<int:pk>/', FaqAdminViews.as_view({'get': 'retrieve'})),
]