from django.urls import path

from goods.views import GoodsListView, ProductDetailView

app_name = 'goods'


urlpatterns = [
    path('', GoodsListView.as_view(), name='index'),
    path('product/<slug:product_id>/', ProductDetailView.as_view(), name='product'),
]