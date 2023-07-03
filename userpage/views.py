from django.shortcuts import render,redirect
from location_data.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def homepage(request):
    provinces=Province.objects.all().order_by('id')[:8]
    context={
        'provinces':provinces
    }
    return render(request,'userpage/home.html',context)

def register_user(request):
    if request.method=='POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'new account created')
            return redirect('/registeruser')
        else:
            messages.add_message(request,messages.ERROR,'failed to add user')
            return render(request,'userpage/register.html',{'forms':form})
    
    context={
        'forms':UserCreationForm
    }
    return render(request,'userpage/register.html',context)


def login_user(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(request, username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                if user.is_staff:
                    return redirect('/admins/dashboard')
                else:
                    return redirect('/')
            else:
                messages.add_message(request,messages.ERROR,'usename and password doesnot match' )
                return render(request,'userpage/login.html',{'forms':form})
    context={
        'forms':LoginForm
    }
    return render(request,'userpage/login.html',context)


def log_out(request):
    logout(request)
    return redirect('/')