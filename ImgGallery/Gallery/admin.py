from django.contrib import admin
from.models import *
# Register your models here.
admin.site.register(Images) #when using inbuilt GUI Admin CRUD functions
#@admin.register(Images)
#class ImagesAdmin(models.ModelAdmin):
