from django.db import models

# Create your models here.
class ForecastModel(models.Model):
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    city = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"[{self.lat}, {self.lon}, {self.city}]"
