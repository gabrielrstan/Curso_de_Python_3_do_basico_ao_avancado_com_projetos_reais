from django.urls import path  # type: ignore

from order.views import Detail, List, Pay, SaveOrder

app_name = 'order'

urlpatterns = [
    path('pay/<int:pk>', Pay.as_view(), name='pay'),
    path('saveorder/', SaveOrder.as_view(), name='saveorder'),
    path('list/', List.as_view(), name='list'),
    path('detail/<int:pk>', Detail.as_view(), name='detail'),
]
