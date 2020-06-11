from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .photoshoot import Photoshoot
from .employee import Employee

class PhotoshootStaff(models.Model):
    
    photoshoot = models.ForeignKey(Photoshoot, on_delete=models.CASCADE) 
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE) 
    
    class Meta:
        verbose_name = ("PhotoshootStaff")
        verbose_name_plural = ("PhotoshootStaffs")        
        
    def __str__(self):
        return f"PhotoshootStaff: {self.employee}"
    
    def get_absolute_url(self):
        return reverse("photoshootstaff_detail", kwargs={"pk": self.pk})