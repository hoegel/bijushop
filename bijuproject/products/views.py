from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from . import models


class HomePageView(TemplateView):
    template_name = 'home.html'

class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'product_detail.html'

class ProductListView(ListView):
    model = models.Product
    template_name = 'product_list.html'

class ProductCreateView(UserPassesTestMixin, CreateView):
    model = models.Product
    fields = '__all__'
    template_name = 'product_new.html'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser