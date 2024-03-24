from django.db import models
from django.utils import timezone


class Worker(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)
        db_table = 'worker'


class Unit(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('-id',)
        db_table = 'unit'


class Visit(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)

    def __str__(self):
        return f"Visit at {self.unit.name} on {self.datetime}"

    class Meta:
        ordering = ('-id',)
        db_table = 'visit'
