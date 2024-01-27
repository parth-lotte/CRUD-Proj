from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record

from django import forms 

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# Make a class to register User / Create user 

class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model= User
        fields= ['username', 'password1', 'password2']
        
        
        
#  Login a user 

class LoginForm(AuthenticationForm):
    
    username= forms.CharField(widget=TextInput())
    password= forms.CharField(widget=PasswordInput())
    
    
    
    
    
#  Record creating 
class CreateRecordForm(forms.ModelForm):
    
    class Meta:
        
        model= Record
        fields= ['first_name', 'last_name', 'email' , 'phone' ,'address', 'city' , 'province', 'country' ]
        
        

#  Record updating 
class UpdateRecordForm(forms.ModelForm):
    
    class Meta:
        
        model= Record
        fields= ['first_name', 'last_name', 'email' , 'phone' ,'address', 'city' , 'province', 'country' ]        