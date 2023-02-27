from django.shortcuts import render,redirect

from .forms import CustomUserCreationForm , ProfileForm
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


def update_profile(request,pk):
    user = User.objects.get(id=pk)
    profile = Profile.objects.get(user=user)
    form = ProfileForm(instance=profile)
    
    

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            user.first_name=request.POST['name']
            user.last_name=request.POST['last_name']
            user.email=request.POST['email']
            user.username=request.POST['username']
            user.save()
            form.save()
            return redirect("login")
        
    context ={'form':form}
    return render(request,"edit_profile.html",context)


def delete_account(request,pk):
    profile = Profile.objects.get(id=pk)

    if request.method=='POST':
        profile.delete()
        return redirect("register")

    return render(request,"delete_user.html")
    


    





