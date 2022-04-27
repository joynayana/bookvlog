from django.contrib import admin
from . models import *
# Register your models here.

class catagdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(categ,catagdmin)

class productadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug','author','price','stock','category','img','available']
    list_editable = ['price','stock','available','img']
admin.site.register(product,productadmin)