from django.contrib.auth.views import LogoutView 
from django.urls import path ,reverse
from .views import login_page,register_page,guest_login_page

app_name = 'accounts'
urlpatterns = [
    
    path('login/',login_page,name = 'login-page'),
    path('register/',register_page,name = 'register-page'),
    path('logout/',LogoutView.as_view(),name='logout'), #Logout 
    path('register/guest/',guest_login_page, name='register-guest')
]