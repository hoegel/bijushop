from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
from products.models import Product
from .cart import Cart

class CartAddView(View):
    def post(self, request, slug):
        cart = Cart(request)
        product = get_object_or_404(Product, slug=slug)
        quantity = int(request.POST.get('quantity', 1))
        override_quantity = request.POST.get('override_quantity', False) == 'True'
        cart.add(product=product, quantity=quantity, override_quantity=override_quantity)
        return redirect('cart:cart_detail')

class CartRemoveView(View):
    def post(self, request, slug):
        cart = Cart(request)
        product = get_object_or_404(Product, slug=slug)
        cart.remove(product)
        return redirect('cart:cart_detail')

class CartDetailView(TemplateView):
    template_name = 'detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        context['cart'] = cart
        return context