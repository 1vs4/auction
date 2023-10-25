from django.urls import path

from goods.views import GoodsView

app_name = 'goods'


urlpatterns = [
    path('', GoodsView.as_view(), name='goods'),

]