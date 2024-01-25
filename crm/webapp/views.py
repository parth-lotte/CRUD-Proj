from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm

# for Login page and authentication 
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate

# from django.http import HttpResponse 

from django.contrib.auth.decorators import login_required

def home(request):
    # return HttpResponse('Hello Parth Lotte !')
    
    return render(request, 'webapp/index.html')



# -- Register 

def register(request):
    
    form= CreateUserForm()
    
    if request.method=="POST":
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('my-login') # redirect to the login page 
            

    context= {'form':form}
    
    return render(request, 'webapp/register.html', context=context)



# Login - Page 

def my_login(request):
    
    form= LoginForm()
    
    if request.method=="POST":
        form= LoginForm(request, data=request.POST)
        
        if form.is_valid():
            
            username= request.POST.get('username')
            password= request.POST.get('password')
            
            user= authenticate(request, username=username , password=password)
            
            if user is not None:
                
                auth.login(request, user)
                
                return redirect("dashboard")
                 
    context= {'form2':form}

    return render(request, 'webapp/my-login.html', context=context)


#  User Log Out 

def user_logout(request):
    auth.logout(request)
    
    return redirect("my-login")

# DashBoard

# we will be giving the route name to the following 

@login_required(login_url='my-login')
def dashboard(request):
    return render(request, 'webapp/dashboard.html')
