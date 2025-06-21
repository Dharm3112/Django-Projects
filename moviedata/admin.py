from django.contrib import admin
from .models import *

# Register your models here.



class showcategory(admin.ModelAdmin):
    list_display = ["name","description"]

admin.site.register(category,showcategory)



class showmaleactor(admin.ModelAdmin):
    list_display = ["name","dob","description"]

admin.site.register(maleactor,showmaleactor)



class showfemaleactor(admin.ModelAdmin):
    list_display = ["name","dob","description"]

admin.site.register(femaleactor,showfemaleactor)



class showmovie(admin.ModelAdmin):
    list_display = ["name","description","actor","actress","moviecategory"]

admin.site.register(movie,showmovie)



class showmultiplex(admin.ModelAdmin):
    list_display = ["name","address","city","state","website"]

admin.site.register(multiplex,showmultiplex)



class showshows(admin.ModelAdmin):
    list_display = ["moviename","multiplexname","showtime","seats","price","type","language"]

admin.site.register(shows,showshows)