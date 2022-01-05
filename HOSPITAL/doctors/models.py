from django.db import models

# Create your models here.
class junnu(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=250)
    address=models.TextField()
    phone=models.BigIntegerField()
    def __str__(self):
        return self.name
