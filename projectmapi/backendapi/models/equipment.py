from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .equipmenttype import EquipmentType
from .batterytype import BatteryType
from .rentalhouse import RentalHouse


class Equipment(models.Model):
    
    name = models.CharField(null = False, max_length = 100) 
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)
    weight = models.FloatField(null=True)
    battery_count = models.IntegerField(null=True)
    battery_type = models.ForeignKey(BatteryType, on_delete = models.CASCADE)
    wireless = models.BooleanField(null=False)
    rental_house = models.ForeignKey(RentalHouse, on_delete=models.CASCADE)
    return_date = models.DateField(null=True)

    
    class Meta:
        verbose_name = ("Equipment")
        verbose_name_plural = ("Equipments")        
        
    def __str__(self):
        return f"Equipment: {self.name}"
    
    def get_absolute_url(self):
        return reverse("equipment_detail", kwargs={"pk": self.pk})