from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('catalog/', views.ProductListView.as_view(), name = 'catalog'),
    path('catalog/new/', views.ProductCreateView.as_view(), name = 'product_new'),
    path('catalog/<slug:slug>/', views.ProductDetailView.as_view(), name = 'product_detail'),
]
