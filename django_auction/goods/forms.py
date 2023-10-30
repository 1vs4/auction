from django.forms import ModelForm
from django import forms

from goods.models import Product


class ProductOfferMoreForm(ModelForm):
    price = forms.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Product
        fields = ('price',)
