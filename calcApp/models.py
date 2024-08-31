from django.db import models

class calcData(models.Model):
    brand=models.CharField(max_length=255)
    model=models.CharField(max_length=255)
    Vehicle_Class=models.CharField(max_length=255)
    Engine_Size=models.IntegerField()
    Cylinder=models.IntegerField()
    Transmission=models.CharField(max_length=255)
    Fuel_Type=models.CharField(max_length=255)
    Fuel_Consumption=models.CharField(max_length=255)




    def __str__(self): 
        return self.brand + "-" + self.model + "-" + self.Fuel_Consumption

