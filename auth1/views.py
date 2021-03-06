from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.template import RequestContext
from django.contrib import messages
from .forms import SignUpForm,EditProfileForm,ProfileForm
from .models import Profile
from cards.models import Cards

# Create your views here.
def home(request):
	# print (request)
	cards = Cards.objects.all()
	return render(request,'home.html',{'cards':cards})
def login_user(request):
	if request.method =='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request,('you have been logged in'))
			return redirect('home')
		else:
			messages.success(request,('Error login in log in with valid username..'))
			return redirect('login')
	else:
		return render(request,'login.html',{})

def logout_user(request):
    logout(request)	
    messages.success(request,('you ave been successfully Logged Out'))
    return redirect('home')	
def register_user(request):
	if request.method =='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']   
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)	
			login(request, user)
			messages.success(request,('you have been successfully registered in'))
			return redirect('home')			
	else:
		form = SignUpForm()
	context={'form':form}
	return render(request,'register.html',context)


def change_password(request):
	if request.method =='POST':
		form = PasswordChangeForm(data=request.POST,user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			messages.success(request,('you have been successfully registered in'))
			return redirect('home')			
	else:
		form = PasswordChangeForm(user=request.user)
	context={'form':form}
	return render(request,'change_password.html',context)


