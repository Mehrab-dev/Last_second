from django.contrib import admin
from .models import ForeignTour , OriginCity , DestinationCity , Hotel

class HotelAdmin(admin.ModelAdmin) :
    list_display = ['id','name','city','star']

class ForeignTourAdmin(admin.ModelAdmin) :
    list_display = ['id','user','duration_of_stay']

admin.site.register(OriginCity)
admin.site.register(DestinationCity)
admin.site.register(Hotel,HotelAdmin)
admin.site.register(ForeignTour,ForeignTourAdmin)