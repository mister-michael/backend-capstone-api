from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .equipmenttype import EquipmentType
from .batterytype import BatteryType
from .rentalhouse import RentalHouse


class Equipment(models.Model):
    
    name = models.CharField(null = False, max_length = 100) 
    equipment_type = models.ForeignKey(EquipmentType, null=True, on_delete=models.SET_NULL)
    weight = models.FloatField(null=True)
    battery_count = models.IntegerField(null=True)
    battery_type = models.ForeignKey(BatteryType, null=True, on_delete = models.SET_NULL)
    wireless = models.BooleanField(null=False)
    rental_house = models.ForeignKey(RentalHouse, null=True, on_delete=models.SET_NULL)
    return_date = models.DateField(null=True)

    
    class Meta:
        verbose_name = ("Equipment")
        verbose_name_plural = ("Equipments")        
        
    def __str__(self):
        return f"Equipment: {self.name}"
    
    def get_absolute_url(self):
        return reverse("equipment_detail", kwargs={"pk": self.pk})