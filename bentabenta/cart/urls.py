from django.urls import path,reverse   
from .views import cart_view,cart_home_view ,cart_update,checkout_home

app_name='cart'
urlpatterns=[
 #   path('cart/',cart_home_view,name='cart'),
   path('cart/',cart_home_view ,name = 'cart-home'),
   path('cart/update/',cart_update,name = 'cart-update'),
   path('checkout/',checkout_home , name = 'checkout'),    
]