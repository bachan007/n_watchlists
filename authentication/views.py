from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'authentication/index.html')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        pwd=request.POST['password']

        usr = authenticate(username=username,password=pwd)

        if usr is not None:
            login(request, usr)
            return render(request,'authentication/index.html',{"u_name":username})
        else:
            messages.error(request,"Username-Password do not match")
            return redirect("home")
    return render(request, 'authentication/signin.html')

def signup(request):

    if request.method == 'POST':
        # email = request.POST['email']
        email = request.POST.get('email')
        username = request.POST['username']
        pwd = request.POST['password']
        confirm_pwd = request.POST.get('confirm_password')
        # print(email.username,pwd,confirm_pwd)

        user = User.objects.create_user(username,email,pwd)
        user.save()

        messages.success(request, 'Your account have been created.')

        return redirect('signin')

    return render(request, 'authentication/signup.html')

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully.")
    return render(request, 'authentication/signup.html')