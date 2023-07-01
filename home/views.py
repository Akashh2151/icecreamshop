# from django.http import HttpResponse
# import email
from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    context={
        'variable1':"this is sent",
        'variable2':"sencond variable pathvle page la"
    }
    # return HttpResponse("this is home page")
  
    return render(request,'index.html',context)

def about(request):
    # return HttpResponse("this is about page")
       return render(request,'about.html')
def icecream(request):
    # return HttpResponse("this is about page")
       return render(request,'icecream.html')

def services(request):
    # return HttpResponse("this is services page")
       return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save() 
        messages.success(request, 'Your massge has been sent')
    # return HttpResponse("this is contact page")
    return render(request,'contact.html')

# def loginuser(request):
#   if request.method=="POST":
#     username=request.POST.get('username')
#     password=request.POST.get('password')
#     print(username,password)
#     user = authenticate(username=username,password=password)
    
#     if user is not None:
#       login(request,user)
#       return redirect("/")
    
#     else:
#        return render(request,'login.html')


#   return render(request,'login.html')