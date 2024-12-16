from .cart import Cart

#чтобы с любой страницы было видно количество товаров в корзине
def cart_context(request):
    cart = Cart(request)
    return {'cart': cart}