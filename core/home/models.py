from django.db import models

# Create your models here.
class Student(models.Model):
   # id =models.AutoField()#this adds  implicitly by the django
    name =models.CharField(max_length =100)
    age =models.IntegerField()
    email =models.EmailField()
    address =models.TextField()
   


class Car(models.Model):
    car_name =models.CharField(max_length=100)
    car_speed =models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name
