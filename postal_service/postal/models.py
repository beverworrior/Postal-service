from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Parcel(models.Model):
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    address = models.TextField()
    weight = models.FloatField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} to {self.recipient}'
