from django.urls import path
from .views import (
    ProductFeaturedListView,
    ProductFeaturedDetailView,
    ProductDetailView,
    ProductDetailSlugView,
    ProductListView,
    product_list_view,
    product_create_view,
    product_delete_view,
    product_detail_view,
    product_update_view)

app_name = 'products' # this is used when adding a namespace in the url
urlpatterns=[
    path('product/',ProductFeaturedListView.as_view(),name = 'product-featured'),
    path('product/<int:id>/',ProductFeaturedDetailView.as_view(),name = 'product-featured'),

#    path('products/',product_list_view , name ='product-list'),
    path('products/',ProductListView.as_view() , name = 'product-view'),
    path('products/create/',product_create_view,name='product-create'),
#    path('products/<int:id>/',product_detail_view,name = 'product-detail'),
    path('products/<int:id>/delete/', product_delete_view, name = 'product-delete'),
    path('products/<int:id>/update/', product_update_view, name = 'product-update'),
    #path('products/<int:id>/',ProductDetailView.as_view(),name ='product-details'),
    path('products/<slug:slug>/',ProductDetailSlugView.as_view(),name ='product-detail'),
   # re_path(r'^product/(?pk<id>\w+)/$', ProductDetailView, name='product-detail'),
]
