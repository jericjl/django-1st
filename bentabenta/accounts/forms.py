from django import forms
from django.contrib.auth import get_user_model

User = get_user_model() # check the documentation for this function is use for registation


class GuestForm(forms.Form):
    email       = forms.EmailField(widget = forms.TextInput(
            attrs={ 
                "class": "form-control" , "placeholder": "Email"
                        }
                    )
                    )


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




class LoginForm(forms.Form):
    username    = forms.CharField(
        widget = forms.TextInput(
            attrs={ 
                "class": "form-control" , "placeholder": "Enter Username"
                        }
                    )
                    , label =''
                    )
    password    = forms.CharField(
        widget = forms.PasswordInput(
            attrs={ 
                "class": "form-control" , "placeholder": "Password"
                        }
                    )
                    , label =''
                    )

class RegisterForm(forms.Form):
    username    = forms.CharField(widget = forms.TextInput(
            attrs={ 
                "class": "form-control" , "placeholder": "Username" 
                }
                )
                , label =''
                )
    email       = forms.EmailField(widget = forms.TextInput(
            attrs={ 
                "class": "form-control" ,"placeholder": "Email"
                }
                )
                , label =''
                )
    password    = forms.CharField(widget=forms.PasswordInput(
        attrs={ 
                "class": "form-control" ,"placeholder": "Password"
                }
                )
                , label =''
                )
    password2   = forms.CharField(widget=forms.PasswordInput(
        attrs={ 
                "class": "form-control" ,"placeholder": "Confirm Password"
                }
                )
                , label =''
                )

#validation and verification

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username = username)
        if qs.exists():
            raise forms.ValidationError("Username is already taken")
        return username

    def clean(self):
        data        = self.cleaned_data
        password    = self.cleaned_data.get('password')
        password2   = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("password must match")
        return data