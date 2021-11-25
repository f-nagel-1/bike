from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=70) 
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=60)

class VehicleType(models.Model):
    name = models.CharField(max_length=60)

class VehicleSize(models.Model):
    name = models.CharField(max_length=60)

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE) #(foreign key to Vehicle Type model)
    date_created = models.DateField()
    real_cost = models.IntegerField()
    size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE) #(foreign key to Vehicle Size model)

class Rental(models.Model):
    rental_date = models.DateField()
    return_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)    #(FK to Customer)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)      #(FK to Vehicle)

class RentalRate (models.Model):
    daily_rate = models.IntegerField() 
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE) #(FK to Vehicle Type)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE) #(FK to Vehicle Size)