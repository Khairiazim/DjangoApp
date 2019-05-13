from django.db import models

# Create your models here.
class Packages(models.Model):
    package_name = models.CharField(max_length=200)
    package_summary = models.TextField
    package_price = models.DecimalField(max_digits=5, decimal_places=2)
    package_period = models.IntegerField
