from django.contrib import admin
from . models import *

class cateadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)} 
   

admin.site.register(categ,cateadmin)

class prodadmin(admin.ModelAdmin):
    list_display=['name','slug','price','img','stock']
    list_editable=['price','stock','img']
    prepopulated_fields={'slug':('name',)}

admin.site.register(products,prodadmin)

# Register your models here.
