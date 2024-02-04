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