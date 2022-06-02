from django import forms  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  
  
class SignupForm(UserCreationForm):  
    email = forms.EmailField(max_length=200, help_text='Required')  
    class Meta:  
        model = User  
        fields = ('username', 'email', 'password1', 'password2')  
        
class LoginForm(forms.Form):
    username = forms.CharField( help_text='Required',
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password = forms.CharField( help_text='Required',
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )