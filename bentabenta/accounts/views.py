from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render

# Create your views here.

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form' : form
    }
 
    if form.is_valid():
        print(form.cleaned_data)
        login_user = form.cleaned_data.get("username")
        login_passwd = form.cleaned_data.get("password")       
        user = authenticate(request,username=login_user, password=login_passwd)
        print(user)
        if user is not None:
            print(request.user.is_authenticated)
            print(user)
            login(request,user)
            context['form'] = LoginForm()
            return redirect("/page/login")
        else:
            print("error")
        
    return render(request , 'pages/pages_login.html',context)

#Registation View function

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context= {
        'form' : form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email    = form.cleaned_data.get("email")
        password = form.cleaned_dataget("password")
        new_user = User.objects.create_user(username,email,password) #check the documentation for this function and get_user_model
        print(new_user)
    return render(request , 'pages/pages_register.html',context)
