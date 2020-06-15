from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class RentalHouse(models.Model):
    
    name = models.CharField(null = False, max_length = 100) 
    city = models.CharField(null = False, max_length = 50)
    phone = models.CharField(null = False, max_length = 20)
    email = models.CharField(null = False, max_length = 60)
    
    class Meta:
        verbose_name = ("RentalHouse")
        verbose_name_plural = ("RentalHouses")        
        
    def __str__(self):
        return f"RentalHouse Id: {self.name}"
    
    def get_absolute_url(self):
        return reverse("rentalhouse_detail", kwargs={"pk": self.pk})