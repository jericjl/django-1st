from django.urls import path,reverse
from .views import home_view ,contact_page_view
app_name ='pages'
urlpatterns =[
    path('',home_view, name ='home-page'),
    path('page/contact/',contact_page_view,name = 'contact-page'),
]
