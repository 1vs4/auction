from django.urls import path

from goods.views import GoodsListView

app_name = 'goods'


urlpatterns = [
    path('', GoodsListView.as_view(), name='index'),

]