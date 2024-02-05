from django.contrib import admin
from librarian.models import user_new,books
# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display=('Username','Email','Register_number','Login_as')

admin.site.register(user_new,userAdmin)

class user_B_Admin(admin.ModelAdmin):
    list_display=('BookName','BookId','Author','BookStatus')

admin.site.register(books,user_B_Admin)