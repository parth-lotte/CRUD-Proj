from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

# for Login page and authentication 
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate

# from django.http import HttpResponse 

from django.contrib.auth.decorators import login_required

from .models import Record

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
    my_records= Record.objects.all( )
    context={'records': my_records}
    return render(request, 'webapp/dashboard.html' , context=context)


# Create a record 

@login_required(login_url='my-login')
def create_record(request):
    
    form= CreateRecordForm()
    
    
    if request.method=="POST":
        form=CreateRecordForm(request.POST)
        
        #  check the validity of the form 
        if form.is_valid():
            
            form.save()
            
            return redirect("dashboard")
        
        
    context={'form':form}
    
    return render(request, 'webapp/create-record.html', context=context)





#  Uopdate Record 
@login_required(login_url='my-login')
def update_record(request, pk):
    
    record=Record.objects.get(id=pk)
    
    form= UpdateRecordForm(instance=record)
    
    if request.method=='POST':
        
        form= UpdateRecordForm(request.POST, instance= record)
        
        if form.is_valid():
            form.save()
            
            return redirect('dashboard')
        
        
        
        
        
    context= {'form':form}
    
    
    
    
    return render(request, 'webapp/update-record.html', context=context)
            
        
    
#  Read or view single record 

@login_required(login_url='my-login')

def read_record(request, pk):
    
    all_records=Record.objects.get(id=pk)
    
    context={'record': all_records}
    
    return render(request,'webapp/view-record.html', context=context)
    
    