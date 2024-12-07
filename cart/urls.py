from django.urls import path
from .views import AddToCartView, CheckoutView, GenerateDiscountView, AnalyticsView

urlpatterns = [
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/checkout/', CheckoutView.as_view(), name='checkout'),
    path('admin/discount/generate/', GenerateDiscountView.as_view(), name='generate-discount'),
    path('admin/analytics/', AnalyticsView.as_view(), name='analytics'),
]
