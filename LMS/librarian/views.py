from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import user_new

result=[]
def index(request):
    return render(request, 'librarian/index.html')
def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        # print(result[0].Username)
        # print(result[0].Register_number)
        # print(result[0].Email)
        # print(result[0].Login_as)
        user=authenticate(request,username=username,password=pass1)
        
        if user is not None:
            result=user_new.objects.filter(Username=username)
            data=result[0]
            login(request,user)
            # request.session['user_data']=data
            if data.Login_as=='User':
                return render(request, 'librarian/user.html',{'user':data})
            elif data.Login_as=='Librarian':
                return render(request, 'librarian/librarian.html',{'user':data})
            elif data.Login_as=='Admin':
                return render(request, 'librarian/index.html',{'user':data})
        else:
            return HttpResponse("username or password is incorrect")
        
        
    return render(request, 'librarian/login.html')
def register(request):
    if request.method=='POST':
        username=request.POST.get('UserName')
        # userid=request.POST.get('User_ID')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirmPassword')
        Login_As=request.POST.get('role')
        RegisterNo=request.POST.get('regno')

        my_user=User.objects.create_user(username,email,pass1)
        my_user.save()

        user=user_new(Username=username,
                      Email=email,
                      Register_number=RegisterNo,
                      Login_as=Login_As)
        # print('login as=',Login_As)
        user.save()
        
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
def tables(request):
    return render(request, 'librarian/tables.html')
def books(request):
    return render(request, 'librarian/books.html')
def profile(request):
    usernm=request.user.username
    result=user_new.objects.filter(Username=usernm)
    data=result[0]
    return render(request, 'librarian/profile.html',{'user_details':data})
def analytics(request):
    return render(request, 'librarian/analytics.html')

def user_index(request):
    return render(request, 'librarian/user.html')
<<<<<<< HEAD
def lib(request):
    return render(request, 'librarian/librarian.html')
=======
def rules(request):
    return render(request, 'librarian/r.html')
def feedback(request):
    return render(request, 'librarian/feedback.html')
>>>>>>> ee300f917b097414573bcf7853df2c288f7c5cab
