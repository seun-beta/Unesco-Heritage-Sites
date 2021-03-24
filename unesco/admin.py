from django.contrib import admin
from unesco.models import Category, Site, Region, Iso, State

admin.site.register(Site)   
admin.site.register(Category)
admin.site.register(Region)
admin.site.register(Iso)
admin.site.register(State)
