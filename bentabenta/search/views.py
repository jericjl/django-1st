from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from products.models import  Products
# Create your views here.


class SearchProductView(ListView):
    template_name ="search/search_view.html"
    def get_context_data(self,*args,**kwargs):
        context = super(SearchProductView,self).get_context_data(*args,**kwargs)
        context['query'] = self.request.GET.get('q')
        return context    
    def get_queryset(self,*args ,**kwargs):
        request = self.request
        print(request.GET)
        query = request.GET.get('q')
        if query is not None:
            #lookups = Q(name__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query) | Q(tag__name__icontains=query) # this is use for search in multiple rows from table
            #return Products.objects.filter(lookups).distinct()
            return Products.objects.search(query)
        return Products.objects.feature()
    
    #   __icontains = field contains this
    #   __iexact    = fields is exactly this