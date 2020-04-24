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


