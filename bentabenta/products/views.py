from django.shortcuts import render,get_object_or_404
from .models import Products
from .forms import ProductCreateForm
# Create your views here.


# List all products
def product_list_view(request):
    item = Products.objects.all()
    context={
        'obj' : item
    }
    return render(request,'products/product_list.html',context)


#Create new Product or Add new Product Function 
def product_create_view(request):
    create_form = ProductCreateForm()
    if request.method == "POST":
        create_form = ProductCreateForm(request.POST)
        if create_form.is_valid():   
            Products.objects.create(**create_form.cleaned_data)
        else:
            print(create_form.errors)
    context={
        'form' : create_form
    }
    return render(request, 'products/product_create.html',context)


def product_detail_view(request ,pid):
    item = Products.objects.get(id=pid)
    context = {
        'obj' : item
    }
    return render(request,'products/product_detail.html',context)


# Update product Details
def product_update_view(request):
    
    context={

    }
    return render(request,'products/product_update.html',context)


# Delete Product
def product_delete_view(request,pid):
    item = get_object_or_404(Products, id = pid)
    if request.method == 'POST':
        item.delete()
    context={
        "obj" : item
    }    
    return render(request ,'products/product_delete.html',context)