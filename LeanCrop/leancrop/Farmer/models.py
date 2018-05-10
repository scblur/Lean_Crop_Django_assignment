from django.db import models
import datetime

# Create your models here.
LANGUAGE_CHOICE = (
            ('English','English'),
            ('Hindi','Hindi'),
            )

class FarmerData(models.Model):
    name = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=12)
    language = models.CharField(max_length=20,choices=LANGUAGE_CHOICE, default='English')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class FarmData(models.Model):
    farmer = models.ForeignKey(FarmerData, on_delete=models.CASCADE, default=1  )
    area = models.CharField(max_length=256)
    village = models.CharField(max_length=256)
    crop_grown = models.CharField(max_length=256)
    sowing_date = models.DateField(("Sowing Date"), default=datetime.date.today)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.village

QUANTITY_UNIT_CHOICE = (
            ('ton','ton'),
            ('kg','kg'),
            ('g (Solid)','g'),
            ('L (Liquid)','L'),
            ('mL (Liquid)','mL'),
            )

class ScheduleData(models.Model):
    farmer = models.ForeignKey(FarmerData, on_delete=models.CASCADE, default=1)
    farmer_farm = models.ForeignKey(FarmData, on_delete=models.CASCADE, default=1)
    days_after_sowing = models.DateField(("Days After Sowing"), default=datetime.date.today)
    fertilizer = models.CharField(max_length=256)
    quantity = models.IntegerField()
    quantity_unit = models.CharField(max_length=20,choices=QUANTITY_UNIT_CHOICE, default='ton')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.days_after_sowing)
