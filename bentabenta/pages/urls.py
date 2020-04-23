from django.urls import path,reverse
from .views import home_view ,login_page,contact_page_view,register_page_view

app_name ='pages'
urlpatterns =[
    path('',home_view, name ='home-page'),
    path('page/login/',login_page,name='login-page'),
    path('page/contact/',contact_page_view,name = 'contact-page'),
    path('page/register/',register_page_view,name = 'register-page')
]
