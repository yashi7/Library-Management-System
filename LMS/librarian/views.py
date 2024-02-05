from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import datetime
from .models import user_new,books,user_with_books
from django.utils.dateparse import parse_date
result=[]
book=[]
def index(request):
    return render(request, 'home/index.html')
def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        
        user=authenticate(request,username=username,password=pass1)
        
        if user is not None:
            result=user_new.objects.filter(Username=user)
            data1=result[0].Login_as
            print(result[0])
            print('username:',result[0].Username)
            print(data1)
            if user.is_superuser:
                return adminpanel(request)  
            elif data1=='User':
                print('logged in as user')
                result=user_new.objects.filter(Username=username)
                data=result[0]
                login(request,user)
                return user_index(request)
            elif data1=='Librarian':
                print('logged in as librarian')
                result=user_new.objects.filter(Username=username)
                data=result[0]
                login(request,user)
                return lib(request)
            else:
                return HttpResponse("username or password is incorrect")
        
        
    return render(request, 'home/login.html')
def register(request):
    print(request.method)
    if request.method=='POST':
        username=request.POST.get('UserName')
        # userid=request.POST.get('User_ID')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirmPassword')
        Login_As=request.POST.get('role')
        RegisterNo=request.POST.get('regno')

       

        if pass1!=pass2:
            return redirect('registration')

        my_user=User.objects.create_user(username,email,pass1)
        my_user.save()          
        print(my_user,'hello')

        user=user_new(Username=username,
                      Email=email,
                      Register_number=RegisterNo,
                      Login_as=Login_As)
        # print('login as=',Login_As)
        user.save()
        
        return redirect('login')
        

    return render(request, 'home/registration.html')
def aboutus(request):
    return render(request, 'home/about_us.html')
def contactus(request):
    return render(request, 'home/contact_us.html')
def help(request):
    return render(request, 'home/help.html')

def tables(request):
    usernm=request.user.username
    result=user_new.objects.filter(Username=usernm)
    data=result[0]
    book=books.objects.all()
    usernm=request.user.username
    u_det=user_with_books.objects.all()
    
    return render(request, 'librarian/tables.html',{'t_data':book,'lib_details':data,'det':u_det})
def books_page(request):
    
    usernm=request.user.username
    result=user_new.objects.filter(Username=usernm)
    data=result[0]
    if request.method=='POST':
        bookName=request.POST.get('b_name')
        bookId=request.POST.get('b_id')
        author=request.POST.get('a_name')
        bookStatus=request.POST.get('b_status')

        add=books(
            BookName=bookName,
            BookId=bookId,
            Author=author,
            BookStatus=bookStatus
        )
        add.save()
    
    return render(request, 'librarian/add_books.html',{'lib_details':data})
def profile(request):
    usernm=request.user.username
    result=user_new.objects.filter(Username=usernm)
    data=result[0]
    return render(request, 'user/profile.html',{'user_details':data})
def analytics(request):
    usernm=request.user.username
    result=user_new.objects.filter(Username=usernm)
    data=result[0]
    return render(request, 'librarian/analytics.html',{'lib_details':data})

def user_index(request):
    usernm=request.user.username
    result=user_new.objects.filter(Username=usernm)
    data=result[0]
    reg=result[0].Register_number
    u_det=user_with_books.objects.filter(Register_number=reg)
    Total_fine=0
    for i in u_det:
        Total_fine+=int(i.Fine)
    print(u_det)
    return render(request, 'user/user.html',{'user_details':data,'det':u_det,'penalty':Total_fine})

def lib(request):
    usernm=request.user.username
    result=user_new.objects.filter(Username=usernm)
    data=result[0]
    return render(request, 'librarian/librarian.html',{'lib_details':data})
def rules(request):
    return render(request, 'home/r.html')
def feedback(request):
    return render(request, 'home/feedback.html')

def userBooks(request):
    usernm=request.user.username
    result=user_new.objects.filter(Username=usernm)
    data=result[0]
    if request.method=='POST':
        B_id=request.POST.get('b_id')
        B_status=request.POST.get('b_status')
        print(B_id,B_status)
        u_name=request.user.username
        print(u_name)
        res=user_new.objects.filter(Username=u_name)
        res[0]
        regnum=res[0].Register_number
        print(regnum)
        Issue=request.POST.get('isu')
        print(Issue)
        Return=request.POST.get('ret')
        Total_fine=0
        if Return!='':
            Total_fine=calculateFine(Issue,Return)

        print(Return)
        

       
        issues=user_with_books(
            BookId=B_id,
            Register_number=regnum,
            IssuedOn=Issue,
            ReturnedOn=Return,
            Fine=Total_fine
        )
        issues.save()

    book=books.objects.all()
    return render(request, 'user/user_books.html',{'b_details':book,'user_details':data})
def calculateFine(issue_date,return_date):
    
    
    fine_total=0

    issue_obj= parse_date(issue_date)    
    return_obj= parse_date(return_date)

    # Calculate the difference between return_date and issue_date
    days_difference = (return_obj-issue_obj).days-7

    fine_rate_per_day = 10 
    if days_difference<0:
        days_difference=0 
    if days_difference > 0:
        fine_total = days_difference * fine_rate_per_day

    print(f"Fine calculated: {fine_total} for {days_difference} days overdue.")
    return fine_total

def libBook(request):
    usernm=request.user.username
    result=user_new.objects.filter(Username=usernm)
    data=result[0]
    book=books.objects.all()
    return render(request,'librarian/lib_books.html',{'b_details':book,'lib_details':data})
def deletebook(request,id):
    d_book=books.objects.get(BookId=id)
    print(books)
    d_book.delete()
    return redirect('libbooks')
def libprofile(request):
    usernm=request.user.username
    result=user_new.objects.filter(Username=usernm)
    data=result[0]           
    return render(request, 'librarian/lib_profile.html',{'lib_details':data})
def seemore(request):
    return render(request, 'home/seemore.html')
def members(request):
    return render(request, 'home/members.html')
def adminpanel(request):
    return render(request,'admin/admin_panel.html')
def adminBooks(request):
    bookk=books.objects.all()
    return render(request,'admin/admin_books.html',{'book':bookk})
def admintables(request):
    us_stt=user_new.objects.all()
    book_det=user_with_books.objects.all()
    return render(request, 'admin/admin_tables.html',{'us_st':us_stt,'bdet':book_det})
