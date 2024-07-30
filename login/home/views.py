from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import re
# Create your views here.
def index(request):

    return render(request, 'index.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return render (request, 'index.html')

        else :
            return redirect ('signup')
    

    return render(request, 'loginPage.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if (len(password) >= 8 and
            re.search(r"[A-Z]", password) and
            re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) and
            re.search(r"\d", password) and
            (password == cpassword)):
            
            myuser = User.objects.create_user(username,email,password)
            myuser.save()
            return redirect('loginPage')
        
        
    return render(request, 'signup.html')


def profile(request):
    return render(request, 'profile.html')

def logout(request):
    logout(request)
    return redirect('index')