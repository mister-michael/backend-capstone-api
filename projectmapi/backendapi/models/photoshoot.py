from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from client import Client
from safedelete.models import SafeDeleteModel, SOFT_DELETE

class Photoshoot(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    name = models.CharField(null=False, max_length=50)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    location = models.CharField(null=True)
    indoor = models.BooleanField(null=True)
    date_scheduled = models.DateTimeField(null=True)
    charge = models.FloatField(null=True)
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Photoshoot")
        verbose_name_plural = ("Photoshoots")

    def __str__(self):
        return f"Client: {self.name}"

    def get_absolute_url(self):
        return reverse("Photoshoot_detail", kwargs={"pk": self.pk})
