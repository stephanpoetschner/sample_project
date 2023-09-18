from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    accessible_for_handicapped = models.BooleanField(default=False)

class LocationImage(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='location_images/')
