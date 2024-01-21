from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse 

def home(request):
    # return HttpResponse('Hello Parth Lotte !')
    
    return render(request, 'webapp/index.html')
