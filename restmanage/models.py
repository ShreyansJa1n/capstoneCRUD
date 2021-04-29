from django.db import models

# Create your models here.


class dish(models.Model):
    idF = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    ing = models.CharField(max_length=100)
    price = models.IntegerField()
    calories = models.FloatField()
    typev = models.BooleanField()
    chef = models.CharField(max_length=15)
    dateAdded = models.DateField()
    image = models.ImageField(upload_to='dishImages')


class vegetables(models.Model):
    idF = models.AutoField(primary_key=True)
    vegename = models.CharField(max_length=15)
    vegedish = models.ForeignKey(dish, on_delete=models.CASCADE)
