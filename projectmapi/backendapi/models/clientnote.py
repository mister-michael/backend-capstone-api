from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .client import Client
from .employee import Employee

class ClientNote(models.Model):
    
    comment = models.CharField(null = False) 
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("ClientNote")
        verbose_name_plural = ("ClientNotes")        
        
    def __str__(self):
        return f"ClientNote: {self.comment}"
    
    def get_absolute_url(self):
        return reverse("clientnote_detail", kwargs={"pk": self.pk})