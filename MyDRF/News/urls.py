from django.urls import path
from . import views
from .views import ProductDetailView

urlpatterns = [
    path('search/', views.search, name='search'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('weather/', views.weather, name='weather'),
    path('currency/', views.currency, name='currency'),
]