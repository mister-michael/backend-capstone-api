from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from safedelete.models import SafeDeleteModel, SOFT_DELETE

class Client(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    
    first_name = models.CharField(null = False, max_length = 25) 
    last_name = models.CharField(null = False, max_length = 25)
    phone = models.CharField(null = False, max_length = 20)
    email = models.CharField(null = False)
    address = models.CharField(null = True, max_length = 50)
    city = models.CharField(null = True, max_length = 50)
    state = models.CharField(null = True, max_length = 2)
    zip_code = models.CharField(null = True, max_length = 50)
    
    class Meta:
        verbose_name = ("Client")
        verbose_name_plural = ("Clients")        
        
    def __str__(self):
        return f"Client: {self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse("client_detail", kwargs={"pk": self.pk})