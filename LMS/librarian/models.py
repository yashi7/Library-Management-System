from django.db import models
from datetime import datetime,timedelta
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
    BookId= models.CharField(max_length=200)
    BookName=models.CharField(max_length=200)
    Author=models.CharField(max_length=200)
    BookStatus= models.CharField(max_length=200)

class user_with_books(models.Model):
    BookId=models.CharField(max_length=200)
    Register_number=models.CharField(max_length=200)
    IssuedOn=models.DateField()
    ReturnedOn=models.DateField(null=True)
    Fine=models.CharField(max_length=200)
