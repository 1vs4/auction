from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormMixin

from common.views import TitleMixin
from goods.forms import ProductOfferMoreForm
from goods.models import Product, Order
from users.models import User

class IndexView(TitleMixin, TemplateView):
    template_name = 'goods/index.html'
    title = 'Index'


class GoodsListView(TitleMixin, ListView):
    template_name = 'goods/products.html'
    model = Product
    title = 'Goods'

    def get_queryset(self):
        queryset = super().get_queryset()

        for obj in queryset:
            if obj.is_expired():
                obj.is_active = False
                obj.save()


        return queryset



class ProductDetailView(FormMixin, DetailView):
    template_name = 'goods/product.html'
    model = Product
    context_object_name = 'product_obj'
    pk_url_kwarg = 'product_id'
    form = ProductOfferMoreForm
    form_class = ProductOfferMoreForm

    def get_success_url(self):
        return reverse_lazy('goods:product', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid() and form.cleaned_data['price'] > int(self.object.price):
            self.object.price = form.cleaned_data['price']

            self.object.user = request.user
            self.object.save()

            return self.form_valid(form)
        else:
            return self.form_invalid(form)