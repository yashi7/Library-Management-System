from django.shortcuts import render



def index(request):
    return render(request, 'librarian/index.html')
def login(request):
    return render(request, 'librarian/login.html')
def register(request):
    return render(request, 'librarian/login.html')
def aboutus(request):
    return render(request, 'librarian/about_us.html')
def contactus(request):
    return render(request, 'librarian/contact_us.html')
def help(request):
    return render(request, 'librarian/help.html')