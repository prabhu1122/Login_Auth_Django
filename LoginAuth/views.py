
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from myApp import settings
# Create your views here.

#@login_required(redirect_field_name='signin')
def home(request):
  return render(request, 'authentication/index.html')


def signup(request):

  if request.method == "POST":
    username = request.POST['username']
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    password = request.POST['password']
    conf_password = request.POST['conf_password']
    dob = request.POST['dob']
    
    if User.objects.filter(username = username):
      messages.error(request, "danger username already exist, try another username")
      return redirect("signup")
      
    if User.objects.filter(email = email):
      messages.error(request, "danger email already registered, try another email")
      return redirect("signup")
      
    if len(username) > 10:
      messages.error(request, "info Username should not be more than 10 charector.")
      return redirect('signup')
    
    if password != conf_password:
      messages.error(request, "danger Password didn't match.")
      return redirect("signup")
    
    if not username.isalnum():
      messages.error(request, "info Username should contains only Alpha_Numaric.")
      return redirect("signup")
      
    
    myuser = User.objects.create_user(username, email, password)
    myuser.first_name = fname
    myuser.last_name = lname
    myuser.DateField = dob
    
    myuser.is_active = False
    
    myuser.save()
    
    #Email confirmation
    '''
    subject = "Welcome to PrabhuShala- A/c login"
    message = "Hello mrs. +myuser.first_name myuser.last_name + \n Welcome to prabhuShala!!\n Thanks to visiting our website.\n please click the following link in order to activate your account. \n\n Thank You\n Prabhat Yadav"
    from_email = settings.EMAIL_HOST_USER
    to_email_lists = [myuser.email]
    send_mail(subject, message, from_email, to_email_lists, fail_silently = True)
    '''
    messages.success(request, "success account created successfully!!!")
    return redirect('signin')

  return render(request, 'authentication/signup.html')
  

def signin(request):
  
  if request.method == "POST":
    username = request.POST['username']
    pass1 = request.POST['pass1']
    
    user = authenticate(username = username, password = pass1)
    
    if user is not None:
      login(request, user)
      return render(request, 'authentication/index.html')
    else:
      return redirect('home')
  return render(request, 'authentication/signin.html')
  
def signout(request):
  logout(request)
  messages.success(request,"logged out")
  return redirect('home')
