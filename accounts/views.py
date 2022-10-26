from django.shortcuts import get_object_or_404, render,redirect

from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=="POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password1']
        email = request.POST['email']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"usename is taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password2,first_name=first_name,last_name=last_name,email=email)
                user.save()

        else:
            print("password not matched")
            return redirect('register')
        return redirect("/")
    else:
        return render(request,'reg.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def forgot(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
        user=get_object_or_404(User, username=username)
        if user.username == username:
            if password == password2:
                user.set_password(password2)
                user.save()
                return redirect('login')
                
            else:
                print("password is not matched")
                return redirect('login')
    return render(request,'forgot.html')