from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from common.views import TitleMixin
from goods.models import Product


class IndexView(TitleMixin, TemplateView):
    template_name = 'goods/index.html'
    title = 'Index'


class GoodsListView(TitleMixin, ListView):
    template_name = 'goods/product.html'
    model = Product
    title = 'Goods'

