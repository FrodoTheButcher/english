from django.shortcuts import render,redirect

from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login ,authenticate ,logout
from .models import Profile 
# Create your views here.
from django.contrib import messages

def registerUser(request,):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect("login")
    return render(request,"register.html",{"form":form})

def loginUser(request):


    if request.user.is_authenticated:
        return redirect('register')


    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request,'Username does not exist')
        user = authenticate(request,username=username,password=password,email=email)
        if user is not None:
            login(request,user)
            return redirect('register')
        else:
            messages.error(request,'Username or password is incorrect')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect ("login")

def account(request,pk):
    user = User.objects.get(id=pk)
    profile = Profile.objects.get(user=user)

    context = {"profile" : profile}

    return render(request,"account.html",context)
    

    





