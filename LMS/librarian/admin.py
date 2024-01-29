from django.contrib import admin
from librarian.models import user_new
# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display=('Username','Email','Register_number','Login_as')

admin.site.register(user_new,userAdmin)