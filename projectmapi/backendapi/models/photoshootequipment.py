from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .photoshoot import Photoshoot
from .equipment import Equipment

class PhotoshootEquipment(models.Model):
    
    photoshoot = models.ForeignKey(Photoshoot, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("PhotoshootEquipment")
        verbose_name_plural = ("PhotoshootEquipments")        
        
    def __str__(self):
        return f"PhotoshootEquipment: PS: {self.photoshoot}, EQ:{self.equipment}"
    
    def get_absolute_url(self):
        return reverse("photoshootequipment_detail", kwargs={"pk": self.pk})