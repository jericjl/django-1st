from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render ,redirect
from .forms import ContactForm,LoginForm, RegisterForm


# Create your views here.
def home_view(request):
    context = {
        'title'     : "BentaBen",
        'content'   : "Magandang Araw Welcome"
    }
    if request.user.is_authenticated:
        context ={
            'great': "This is great"
        } 
    return render(request , 'pages/pages_home.html',context)

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
def register_page_view(request):
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





#Contact View Function

def contact_page_view(request):
    contact_form = ContactForm(request.POST or None)

    context={
        'title'     : "Contact",
        'form'      :  contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    #if request.method == "POST":
    #    print(request.POST.get('fullname'))
    #    print(request.POST.get('email'))
    #    print(request.POST.get('message'))
    return render(request , 'pages/pages_contact.html',context)


