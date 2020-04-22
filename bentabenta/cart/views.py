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
    products = cart_obj.products.all()
    total = 0
    for x in products:
        total += x.price
    print(total)
    cart_obj.total = total
    cart_obj.save()
    #request.session['cart_id'] = "12"
    #cart_id = request.session.get("cart_id" , None)
    #qs = Cart.objects.filter(id=cart_id)
    #if qs.count() == 1:
    #    cart_obj = qs.first()
    #    print("cart id exist")
    #    if request.user.is_authenticated and cart_obj.user is None:
    #        cart_obj.user = request.user
    #        cart_obj.save()
    #else:
    #    request_user = request.user
    #    cart_obj = Cart.objects.new_cart(user=request_user)
    #    request.session['cart_id'] = cart_obj.id
    return render(request, 'cart/home.html', {} )

def cart_update(request):
    obj = Products.objects.get(id=1)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    cart_obj.products.add(obj)
    #cart_obj.products.remove()
    return redirect("cart:cart-home")
