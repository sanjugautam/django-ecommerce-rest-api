from django.urls import path

from core.views import CustomerList, CustomerDetail, CustomerCreate

urlpatterns = [
    path('customer/create', CustomerCreate.as_view()),
    path('customer/all', CustomerList.as_view()),
    path('customer/<int:pk>', CustomerDetail.as_view()),
]
