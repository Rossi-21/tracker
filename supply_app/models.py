from django.db import models

from django.db import models


class Invoice(models.Model):
    vendor = models.ForeignKey(
        'Vendor', on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(
        'Department', on_delete=models.CASCADE, null=True, blank=True)
    total = models.FloatField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.vendor)


class Vendor(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return str(self.name)


class Department(models.Model):
    name = models.CharField(max_length=128)
    number = models.IntegerField()

    def __str__(self):
        return str(self.name)
