"""
URL configuration for LMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from librarian.views import index,loginpage,aboutus,help,contactus,register, user_index,profile,tables,books,analytics,rules,feedback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('login/',loginpage,name='login'),
    path('aboutus/',aboutus,name='about_us'),
    path('contactus/',contactus,name='contact_us'),
    path('help/',help,name='help'),
    path('resgistration/',register,name='registration'),
    # path('user/',user,name='user'),
    path('user_index/',user_index,name='user_index'),
    path('profile/',profile,name='profile'),
    path('books/',books,name='books'),
    path('tables/',tables,name='tables'),
    path('analytics/',analytics,name='analytics'),
    path('rules/',rules,name='r'),
    path('feedback/',feedback,name='feedback'),
]

