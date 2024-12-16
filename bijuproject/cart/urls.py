from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartDetailView.as_view(), name='cart_detail'),
    path('add/<slug:slug>/', views.CartAddView.as_view(), name='cart_add'),
    path('remove/<slug:slug>/', views.CartRemoveView.as_view(), name='cart_remove'),
]
