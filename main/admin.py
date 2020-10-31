from django.contrib import admin
from main.models import Post,Contact

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'posted_date')

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','message')    

admin.site.register(Post, PostAdmin)
admin.site.register(Contact,ContactAdmin)