from django.db import models
Login = (
    ("admin","admin"),
    ("user", "user"),
    ("librarian", "librarian"),
    
)
 
class user_new(models.Model):
    Username = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Register_number = models.CharField(max_length=200)
    Login_as = models.CharField(max_length=200 ,choices=Login)



