from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def register(request):
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("login_view")
    else:
      return render(request , "register.html",{'form':form})
  form = RegisterForm()
  return render(request , "register.html",{'form':form})

def login_view(request):
  if request.method == "POST":
    uname = request.POST.get("username")
    pword = request.POST.get("password")
    user = authenticate(username=uname, password=pword)
    if(user):
      login(request,user)
      return redirect("student")
    else:
      return render(request , "login.html",{'form':AuthenticationForm()})
  else:
    return render(request , "login.html",{'form':AuthenticationForm()})

def logout_view(request):
  logout(request)
  return redirect("login_view")