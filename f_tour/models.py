from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class OriginCity(models.Model) :
    name = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.name

class DestinationCity(models.Model) :
    name = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.name


class Hotel(models.Model) :
    name = models.CharField(max_length=255)
    star = models.IntegerField()
    city = models.ForeignKey(DestinationCity,on_delete=models.CASCADE,null=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.name,self.city)

    

class ForeignTour(models.Model) :
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    origin = models.ForeignKey(OriginCity,on_delete=models.SET_NULL,null=True)
    destination = models.ManyToManyField(DestinationCity)
    date_gone = models.DateField()
    return_date = models.DateField()
    duration_of_stay = models.IntegerField(blank=True,null=True)
    hotel = models.ManyToManyField(Hotel)


    def save(self,*args,**kwargs) :
        if self.return_date and self.date_gone :
            self.duration_of_stay = (self.return_date - self.date_gone).days
        super().save(*args,**kwargs)

        
    
