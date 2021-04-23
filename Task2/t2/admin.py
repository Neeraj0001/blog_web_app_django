# Register your models here.
from django.contrib import admin
from . models import Profile,Post_all,Post_public,Post_private
admin.site.register(Profile) 
admin.site.register(Post_all) 
admin.site.register(Post_private) 

