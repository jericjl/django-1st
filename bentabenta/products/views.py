from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView
from django.http import Http404
from .models import Products,ProductManager
from .forms import ProductForm
from cart.models import  Cart


# Create your views here.

class ProductFeaturedListView(ListView):
    template_name = "products/featured_list.html"
    def get_queryset(self,*args,**kwargs):
        request=self.request
        return Products.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    #queryset = Products.objects.all().featured() # define a query set in the models
    #print(queryset)
    template_name = 'products/featured_detail.html'
    def get_context_data(self,*args,**kwargs):
        context= super(ProductFeaturedDetailView,self).get_context_data(*args,**kwargs)
        return context
    #get the data from arguments or example from template path ('products/<int:id>')
    def get_object(self,*args,**kwargs):
        request = self.request
        id = self.kwargs.get('id')
        instance = Products.objects.features(id)
        if instance is None:
            raise Http404("Product does not exist")
        return instance

class ProductDetailSlugView(DetailView):
    #queryset = Products.objects.all()
    template_name = 'products/product_detail.html'
    def get_context_data(self,*args, **kwargs):
        context = super(ProductDetailSlugView,self).get_context_data(*args,**kwargs)
        request = self.request
        cart_obj , new_obj = Cart.objects.new_or_get(request)
        context['cart'] = cart_obj
        return context


    def get_object(self,*args,**kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Products.objects.get(slug=slug, active= True)
        except Products.DoesNotExist:
            raise Http404("Not Found")
        except Products.MultipleObjectsReturned:
            qs = Products.objects.filter(slug=slug,active=True)
            instance = qs.first()
        return instance


class ProductDetailView(DetailView):
    #queryset = Products.objects.all()
    template_name = 'products/product_detail.html'
    def get_context_data(self,*args,**kwargs):
        context= super(ProductDetailView,self).get_context_data(*args,**kwargs)
        #print(context)
        return context
    #get the data from arguments or example from template path ('products/<int:id>')
    def get_object(self,*args,**kwargs):
        request = self.request
        id = self.kwargs.get('id')
        instance = Products.objects.get_by_id(id)
        #print(instance)
        if instance is None:
            raise Http404("Product does not exist")
        return instance

class ProductListView(ListView):
    template_name = "products/product_list.html"
    queryset = Products.objects.all()
    #print(queryset)

    #get arguments or data from tempalate
    def get_context_data(self,*args,**kwargs):
        context = super(ProductListView,self).get_context_data(*args,**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
       
     #   print(context)
        return context
    



# List all products
def product_list_view(request):
    item = Products.objects.all() # query
    context={
        'object_list' : item
    }
    return render(request,'products/product_list.html',context)


#Create new Product or Add new Product Function 
def product_create_view(request):
    create_form = ProductForm()
    if request.method == "POST":
        create_form = ProductForm(request.POST)
        if create_form.is_valid():   
            Products.objects.create(**create_form.cleaned_data)
        else:
            print(create_form.errors)
    context={
        'form' : create_form
    }
    return render(request, 'products/product_create.html',context)


#Generic Detail view



# Diplay Product per ID
def product_detail_view(request ,id): #(request ,pid = None ,*args ,**kwargs)

    instance = Products.objects.get_by_id(id)
    qs = Products.objects.filter(id=id)
    if qs.exists() and qs.count() == 1:
        instance = qs.first()
    else:
       raise Http404("Product does not exists")
    if instance is None:
        raise Http404("Product does not exists")
    context = {
        'objects' : instance
    }
    return render(request,'products/product_detail.html',context)




# Update product Details
def product_update_view(request,pid):
    context ={} 
    obj = get_object_or_404(Products,id=pid) 
    form = ProductForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        print('Success')

    context={
        'form':form
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



