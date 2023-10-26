from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from goods.models import Product


class IndexView(TemplateView):
    template_name = 'goods/index.html'


class GoodsListView(ListView):
    template_name = 'goods/products.html'
    model = Product

