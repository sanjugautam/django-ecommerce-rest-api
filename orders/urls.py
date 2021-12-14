from django.urls import path

from orders.views import OrderListAPIView, OrderDetailAPIView

urlpatterns = [
    path('get-or-create/', OrderListAPIView.as_view()),
    path('get-update-delete/<str:pk>/', OrderDetailAPIView.as_view()),
]
