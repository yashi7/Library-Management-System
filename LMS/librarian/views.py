from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'librarian/index.html')
def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('user_index')
        else:
            return HttpResponse("username or password is incorrect")

        
    return render(request, 'librarian/login.html')
def register(request):
    if request.method=='POST':
        username=request.POST.get('UserName')
        # userid=request.POST.get('User_ID')
        Email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirmPassword')

        # if pass1!=pass2:
        # #     return HttpResponse("your password and confirm password are not same!!")
        # else:
        my_user=User.objects.create_user(username,Email,pass1)
        my_user.save()
        
        return redirect('login')
        

    return render(request, 'librarian/registration.html')
def aboutus(request):
    return render(request, 'librarian/about_us.html')
def contactus(request):
    return render(request, 'librarian/contact_us.html')
def help(request):
    return render(request, 'librarian/help.html')
# @login_required
# def user(request):
#     user = request.user  
#     context={'user': user }
#     return render(request,'librarian/user.html')


def user_index(request):
    return render(request, 'librarian/user.html')


