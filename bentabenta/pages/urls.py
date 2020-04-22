from django.urls import path
from .views import home_view ,login_page,contact_page_view,register_page_view


urlpatterns =[
    path('',home_view, name ='home'),
    path('page/login/',login_page,name='login-page'),
    path('page/contact/',contact_page_view,name = 'contact-page'),
    path('page/register/',register_page_view,name = 'register-page')
]
