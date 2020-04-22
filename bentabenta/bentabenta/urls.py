"""bentabenta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings # check the documentation - this is manually added
from django.conf.urls.static import static # check the documentation - this is manually added


from django.contrib import admin
from django.urls import path ,include

from products.views import (
  #  product_list_view,
 #   product_create_view,
 #   product_detail_view,
 #   product_delete_view,
 #   product_update_view,
    ProductFeaturedListView,
    ProductFeaturedDetailView,
    ProductDetailView)

from pages.views import home_view, contact_page_view,login_page
#from cart.views import cart_view,cart_home_view


urlpatterns = [
    path('',include('products.urls',namespace='products')),
    path('',include('pages.urls')),
    path('',home_view,name='home-view'),
    path('',include('cart.urls',namespace = 'cart')),
    path('admin/', admin.site.urls),

    path('product/<int:id>/',ProductDetailView.as_view() , name ='product-list'),
    path('featured/', ProductFeaturedListView.as_view(), name ='featured-list'),
    path('featured/<int:pid>' ,ProductFeaturedDetailView.as_view(),name ='featured-detail'),

    path('', include('search.urls',namespace='search')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
