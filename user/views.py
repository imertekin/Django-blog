from django.shortcuts import render,redirect
from django.contrib import messages
from.forms import RegisterForm,LoginUserForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def register(request):
    

    form=RegisterForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')

        newUser=User(username=username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        return redirect('index')


    context= {

        'form':form
    }

     
    return render(request,"register.html",context)

def loginUser(request):
    form=LoginUserForm(request.POST or None)
    
    context= {

        'form':form
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Kullanıcı adı ya da parola hatalı")
            return render(request,"login.html",context)
    
        messages.success(request,"Başarılı Giriş")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)
def logUserout(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")