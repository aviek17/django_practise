from django.db import models

# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=80)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.car_name} {self.speed} {self.description}"