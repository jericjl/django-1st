from django.shortcuts import render

from products.models import Products



# Create your views here.
def cart_view(request):
    
    #print(request.session)
    context={

    }
    return render(request,'cart/cart_list.html',context)

def cart_home_view(request):
    #print(request.session)
    print(request.session.session_key)
    context= {

    }
    return render(request, 'cart/home.html', context )