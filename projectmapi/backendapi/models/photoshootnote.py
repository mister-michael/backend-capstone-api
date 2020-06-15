from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .photoshoot import Photoshoot
from .employee import Employee

class PhotoshootNote(models.Model):
    
    comment = models.CharField(null = False, max_length=1000) 
    photoshoot = models.ForeignKey(Photoshoot, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("PhotoshootNote")
        verbose_name_plural = ("PhotoshootNotes")        
        
    def __str__(self):
        return f"PhotoshootNote: {self.name}"
    
    def get_absolute_url(self):
        return reverse("photoshootnote_detail", kwargs={"pk": self.pk})