from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class BatteryType(models.Model):
    
    name = models.CharField(null = False, max_length = 100) 
    
    class Meta:
        verbose_name = ("BatteryType")
        verbose_name_plural = ("BatteryTypes")        
        
    def __str__(self):
        return f"BatteryType: {self.name}"
    
    def get_absolute_url(self):
        return reverse("batterytype_detail", kwargs={"pk": self.pk})