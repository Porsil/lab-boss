from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
from datetime import datetime, timedelta


BATCH_STATUS = (("To Test", "To Test"), ("Approved", "Approved"))
MATERIAL_STATUS = (("Active", "Active"), ("Inactive", "Inactive"))


class Material(models.Model):
    name = models.CharField(max_length=25, unique=True)
    status = models.TextField(choices=MATERIAL_STATUS, default="Active")

    def __str__(self):
        return self.name


class Batch(models.Model):
    priority = models.BooleanField(default=False)
    batch = models.CharField(max_length=10, unique=True)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    booked_in = models.DateField(auto_now_add=True)
    comments = models.TextField(blank=True)
    status = models.TextField(choices=BATCH_STATUS, default="To Test")

    class Meta:
        ordering = ['booked_in']

    def __str__(self):
        return self.batch

    def due_date(self):
        return self.booked_in + timedelta(7)
