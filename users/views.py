from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from users.forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.
def register(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid() == True:
			user = form.save()
			return redirect("/")
	else:
		form = SignUpForm()
	context = {"SignUpForm":form}
	return render(request,'users/register.html',context)

def Login(request):
	if request.user.is_authenticated:
		return redirect("/")
#if method
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid() == True:
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			authUser = authenticate(request=request,username = username,password = password)
			if authUser is not None:
				login(request,authUser)
				return redirect("/")
			else:
				messages.error(request,"user name or password is invalid.")
	else:
		form = AuthenticationForm()
	context = {"form":form}
	return render(request,'users/login.html',context)

def Logout(request):
	logout(request)
	return redirect("/")