from django.urls import path  # type: ignore
from order.views import Pay, CloseOrder, Detail

app_name = 'order'

urlpatterns = [
    path('', Pay.as_view(), name='pay'),
    path('closeorder/', CloseOrder.as_view(), name='closeorder'),
    path('detail/', Detail.as_view(), name='detail'),
]
