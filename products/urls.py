from django.urls import path
from products.views import ProductListView, ProductDetailsView

urlpatterns = [
    path('get-or-create/', ProductListView.as_view()),
    path('get-update-delete/<int:pk>/', ProductDetailsView.as_view()),
]