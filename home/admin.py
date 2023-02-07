from django.contrib import admin

from .models import (
    AnimalCategory,
    AnimalBreed,
    AnimalColor,
    
    Animal,
    
    AnimalLocation,
    AnimalImage
)
# Register your models here.

class AnimalAdmin(admin.ModelAdmin):
    list_display = ['owner', 'name', 'category','gender', 'all_breeds', 'all_colors']
    list_display_links = ['owner', 'name']
    

admin.site.register(AnimalCategory)
admin.site.register(AnimalBreed)
admin.site.register(AnimalColor)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(AnimalLocation)
admin.site.register(AnimalImage)
