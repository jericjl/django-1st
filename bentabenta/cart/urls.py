from django.urls import path,reverse   
from .views import cart_view,cart_home_view ,cart_update

app_name='cart'
urlpatterns=[
 #   path('cart/',cart_home_view,name='cart'),
    path('cart/<int:pid>/view/',cart_view , name = 'cart-view'),
    path('cart/',cart_home_view ,name = 'cart-home'),
   path('cart/update/',cart_update,name = 'cart-update'),
    
]