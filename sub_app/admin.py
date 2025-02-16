from django.contrib import admin

# Register your models here.

from sub_app import models

class ImagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

admin.site.register(models.Images, ImagesAdmin)