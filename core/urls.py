from django.urls import path

from core.views import CustomerList, CustomerDetail

urlpatterns = [
    path('customer/', CustomerList.as_view()),
    path('customer/<int:pk>', CustomerDetail.as_view()),
]