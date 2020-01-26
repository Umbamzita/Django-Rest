from django.db import models


class Drink(models.Model):
    title = models.CharField(max_length=50, unique = True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title



class Worker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    drinks = models.ManyToManyField(Drink, through='Sale')
      
    def __str__(self):
        return f'{self.first_name} {self.last_name}' 



class Sale(models.Model):
    s_drink = models.ForeignKey(Drink, on_delete = models.DO_NOTHING)
    s_worker = models.ForeignKey(Worker, on_delete = models.CASCADE )

    def __str__(self):
        return f'{self.s_worker} {self.s_drink}' 

