from django.shortcuts import render,redirect

from products.models import Products
from .models import Cart


# Create your views here.
def cart_view(request):
    
    #print(request.session)
    context={

    }
    return render(request,'cart/cart_list.html',context)

def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    print("New cart created")
    return cart_obj


def cart_home_view(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, 'cart/home.html', {"cart":cart_obj} )

def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Products.objects.get(id=product_id)
        except Products.DoesNotExist:
            print("No Product")
            return redirect("cart:cart-home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
        #obj = Products.objects.get(id=1)
            cart_obj.products.add(product_obj)
        #cart_obj.products.remove()
        return redirect("cart:cart-home")
