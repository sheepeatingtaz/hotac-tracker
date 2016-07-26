from django.db import models

class ImperialShip(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=20, unique=True)
    tie = models.BooleanField(default=False, verbose_name="TIE")
    large = models.BooleanField(default=False)
    icon = models.CharField(max_length=50, blank=True, null=True)
