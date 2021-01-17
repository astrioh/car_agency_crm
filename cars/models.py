from django.db import models

class BodyType(models.Model):
    name = models.CharField(max_length=50)


class Brand(models.Model):
    name = models.CharField(max_length=20)


class CarPhoto(models.Model):
    image = models.ImageField(upload_to='cars')
    car = models.ForeignKey('Cars', on_delete=models.CASCADE)


class CarType(models.Model):
    name = models.CharField(max_length=30)


class Car(models.Model):
    car_model = models.ForeignKey('CarModel', on_delete=models.CASCADE)
    id_dealer = models.ForeignKey('Dealer', on_delete=models.CASCADE)
    pts = models.CharField(max_length=25)
    vin = models.CharField(max_length=25)
    car_type = models.ForeignKey(CarType, on_delete=models.CASCADE)
    release_year = models.SmallIntegerField()
    price = models.DecimalField(max_digits=18, decimal_places=0)
    color = models.CharField(max_length=15)
    mileage = models.IntegerField(blank=True, null=True)
    wheel = models.CharField(max_length=50, blank=True, null=True)
    body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE)
    transmission_type = models.ForeignKey('TransmissionType', on_delete=models.CASCADE)
    drivetrain_type = models.ForeignKey('DrivetrainType', on_delete=models.CASCADE)
    engine_type = models.ForeignKey('EngineTypes', on_delete=models.CASCADE)
    engine_volume = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    engine_power = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)


class DefectType(models.Model):
    name = models.CharField(max_length=30)


class Defect(models.Model):
    defect_type = models.ForeignKey(DefectType, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=350, blank=True, null=True)
    image = models.ImageField(max_length=80, blank=True, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)


class DrivetrainType(models.Model):
    name = models.CharField(max_length=30)

class EngineType(models.Model):
    name = models.CharField(max_length=30)


class CarModel(models.Model):
    name = models.CharField(max_length=80)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

class TransmissionType(models.Model):
    name = models.CharField(max_length=30)