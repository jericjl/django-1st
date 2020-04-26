from django import forms
from django.contrib.auth import get_user_model

User = get_user_model() # check the documentation for this function is use for registation

class ContactForm(forms.Form):
    fullname    = forms.CharField(
        widget = forms.TextInput(
            attrs={ 
                "class": "form-control" , "placeholder": "Your full name"
                        }
                    )
                    )
    email       = forms.EmailField(widget = forms.TextInput(
            attrs={ 
                "class": "form-control" , "placeholder": "Email"
                        }
                    )
                    )
    message     = forms.CharField(widget = forms.Textarea(
            attrs={ 
                "class": "form-control" , "placeholder": "Messages"
                        }
                    )
                    )

# Validation
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be a Gmail")
        return email