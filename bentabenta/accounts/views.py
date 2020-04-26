from django.forms import forms
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render ,redirect
from django.utils.http import is_safe_url
from django.http import HttpResponse
from .models import GuestEmail
from .forms import GuestForm

from .forms import LoginForm, RegisterForm

# Create your views here.
def guest_login_page(request):
    form = GuestForm(request.POST or None)
    context = {
        'form' : form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if redirect_path is None:
        redirect_path = '/' # redirect to home if value is None
    if form.is_valid():
        print(form.cleaned_data)
        email = form.cleaned_data.get("email")
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path ,request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("accounts:register-page")
    return redirect("accounts:register-page")

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form' : form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if redirect_path is None:
        redirect_path = '/' # redirect to home if value is None
    if form.is_valid():
        #print(form.cleaned_data)
        login_user = form.cleaned_data.get("username")
        login_passwd = form.cleaned_data.get("password")       
        user = authenticate(request,username=login_user, password=login_passwd)
        #print(user)
        if user is not None:
            try:
                del request.session['guest_email_id']
            except:
                pass
            print(request.user.is_authenticated)
            print(user)
            login(request,user)
            context['form'] = LoginForm()
            return redirect(redirect_path) # redirectpath when logged in
        else:
            print("error")
            return redirect("pages:home-page")
        
    return render(request , 'accounts/account_login.html',context)

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
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username,email,password) #check the documentation for this function and get_user_model
        print(new_user)
    return render(request , 'accounts/account_register.html',context)
