from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class EquipmentType(models.Model):
    
    name = models.CharField(null = False, max_length = 100) 
    
    class Meta:
        verbose_name = ("EquipmentType")
        verbose_name_plural = ("EquipmentTypes")        
        
    def __str__(self):
        return f"EquipmentType: {self.name}"
    
    def get_absolute_url(self):
        return reverse("equipmenttype_detail", kwargs={"pk": self.pk})