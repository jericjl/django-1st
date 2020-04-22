from django.conf import settings
from django.db import models

from products.models import Products
User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
 #   def get_or_create():
  #      return obj,True

    def new_or_get(self, request):
        cart_id = request.session.get("cart_id" , None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            print("cart id exist")
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            request_user = request.user
            cart_obj = Cart.objects.new_cart(user=request_user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj,new_obj

    def new_cart(self, user=None):
        user_obj=None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)




# Create your models here.
class Cart(models.Model):
    user        = models.ForeignKey(User,null=True, blank=True,on_delete=models.DO_NOTHING)
    products    = models.ManyToManyField(Products,blank=True)
    total       = models.DecimalField(default=0,max_digits=65, decimal_places=2)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)