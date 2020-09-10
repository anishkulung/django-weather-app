from django.contrib import admin
from .models import City,City_cord
# Register your models here.

# admin.site.register(City)
@admin.register(City)
class City(admin.ModelAdmin):
	list_display = ('name',)
# admin.site.register(City_cord)
@admin.register(City_cord) 	
class City_cordAdmin(admin.ModelAdmin):
	list_display = ('city','lat','lon',)
	fields=['city','lat','lon']