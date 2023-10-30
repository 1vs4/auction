from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from common.views import TitleMixin
from goods.models import Product


class IndexView(TitleMixin, TemplateView):
    template_name = 'goods/index.html'
    title = 'Index'


class GoodsListView(TitleMixin, ListView):
    template_name = 'goods/products.html'
    model = Product
    title = 'Goods'



class ProductDetailView(DetailView):
    template_name = 'goods/product.html'
    model = Product
    context_object_name = 'product_obj'
    pk_url_kwarg = 'product_id'

