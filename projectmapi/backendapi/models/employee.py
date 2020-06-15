from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Employee(models.Model):
    
    city = models.CharField(null = False, max_length = 50) 
    phone = models.CharField(null = False, max_length = 20)
    user = models.ForeignKey(User, related_name="employees", on_delete = models.CASCADE)
    
    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")        
        
    def __str__(self):
        return f"Employee Id: {self.user}"
    
    def get_absolute_url(self):
        return reverse("employee_detail", kwargs={"pk": self.pk})