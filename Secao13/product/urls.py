from django.urls import path  # type: ignore
from product.views import (AddToCart, ProductList, PurchaseSummary, Cart,
                           ProductDetail, RemoveFromCart)


app_name = 'product'

urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('<slug>', ProductDetail.as_view(), name='detail'),
    path('addtocart/', AddToCart.as_view(), name='addtocart'),
    path('removefromcart/', RemoveFromCart.as_view(), name='removefromcart'),
    path('cart/', Cart.as_view(), name='cart'),
    path('purchase_summary/', PurchaseSummary.as_view(),
         name='purchasesummary'),
]
