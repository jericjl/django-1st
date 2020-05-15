from django.shortcuts import render,redirect
from accounts.forms import LoginForm, GuestForm
from addresses.forms import AddressForm

from accounts.models import GuestEmail
from billings.models import BillingProfile
from addresses.models import Address
from products.models import Products
from orders.models import Order
from .models import Cart,CartItem


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
    cart_product_qty    = CartItem.objects.filter(cart = cart_obj )
    context = {
        "cart":cart_obj,
        "qty"  : cart_product_qty
        } 
    return render(request, 'cart/home.html',context )
    
def cart_update(request):
    product_id = request.POST.get('product_id')
    qty =1
    if product_id is not None:
        try:
            product_obj = Products.objects.get(id=product_id)
        except Products.DoesNotExist:
            print("No Product")
            return redirect("cart:cart-home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
            CartItem.objects.filter(products=product_obj).delete()
        else:
        #obj = Products.objects.get(id=1)
            cart_obj.products.add(product_obj)
            cartitem_add = CartItem.objects.create(cart=cart_obj, products=product_obj ,quantity=qty) 
        #cart_obj.products.remove()
        request.session['cart_items'] = cart_obj.products.count()
        return redirect("cart:cart-home")


def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    product_count = cart_obj.products.count()
    if cart_created  or product_count == 0:
        return redirect("cart:cart-home")
    login_form      =   LoginForm()
    guest_form      =   GuestForm()
    address_form    =   AddressForm()
    #billing_address_form =  AddressForm()
    billing_address_id = request.session.get("billing_address_id", None)
    shipping_address_id = request.session.get("shipping_address_id", None)
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    address_qs = None
    if billing_profile is not None:
        if request.user.is_authenticated:
            address_qs = Address.objects.filter(billing_profile=billing_profile)
        #models Manager
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile ,cart_obj)
        if shipping_address_id:
            order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
            del request.session['shipping_address_id']
        elif billing_address_id:
            order_obj.billing_address = Address.objects.get(id=billing_address_id)  
            del request.session["billing_address_id"]
        if billing_address_id or shipping_address_id:
            order_obj.save()
       # has_card = billing_profile.has_card
    
    if request.method == "POST":
        is_prepared = order_obj.check_done()
        if is_prepared:
            order_obj.mark_paid() # sort a signal for us
            request.session['cart_items'] = 0
            del request.session['cart_id']
            return redirect("cart:checkout-success")
        else:
 
            return redirect("cart:checkout")

    context =   {
        "object" : order_obj,
        "billing_profile" : billing_profile,
        "login_form"    : login_form,
        "guest_form"    : guest_form,
        'address_form'  : address_form,
        "address_qs"    : address_qs,
    } 
    return render(request, "cart/checkout.html" , context)


def checkout_success_view(request):
    return render(request,'cart/checkout_done.html',{})




