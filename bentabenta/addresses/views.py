from django.shortcuts import render,redirect
from .forms import AddressForm
from django.utils.http import is_safe_url
from billings.models import BillingProfile
from .models import Address

# Create your views here.
def checkout_address_create_view(request):
    form = AddressForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        instance = form.save(commit=False)
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
        if billing_profile is not None:
            address_type = request.POST.get('address_type','shipping')
            instance.billing_profile = billing_profile
            instance.address_type = address_type
            instance.save()
            request.session[address_type + "_address_id"] = instance.id
            billing_address_id = request.session.get("billing_address_id" , None)
            shipping_address_id = request.session.get("shipping_address_id" , None)
            print(address_type + "_address_id")
        else:
            print("Error")
            return redirect ("cart:checkout")
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        
        return redirect("cart:checkout") 


