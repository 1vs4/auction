from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'goods/index.html'


class GoodsView(TemplateView):
    template_name = 'goods/products.html'