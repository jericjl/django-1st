from django.urls import path ,reverse
from .views import login_page,register_page

app_name = 'accounts'
urlpatterns = [
    
    path('login/',login_page,name = 'login-page'),
    path('register/',register_page,name = 'register-page')
]