from django.db import models
Login = (
    ("Admin","Admin"),
    ("User", "User"),
    ("Librarian", "Librarian"),
    
)
 
class user_new(models.Model):
    Username = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Register_number = models.CharField(max_length=200)
    Login_as = models.CharField(max_length=200 ,choices=Login)

class books(models.Model):
    Bookname= models.CharField(max_length=200)
    Bookid= models.IntegerField()
    BookAuthor= models.CharField(max_length=200)
    BookStatus=models.CharField(max_length=200)

class books_with_users(models.Model):
    Bookname=models.CharField(max_length=200)
    Bookid= models.IntegerField()
    Userid=models.IntegerField()
    IssuedOn=models.DateField()
    ReturnedOn=models.DateField()
    Penalty= models.IntegerField()


