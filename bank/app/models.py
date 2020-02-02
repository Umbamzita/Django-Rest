import uuid, os
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator


alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


def customer_photo(instance, filename):
    typ = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{typ}'
    return os.path.join(os.getcwd()+'\\media', filename) 

class Customer(models.Model):

    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    passport = models.CharField(max_length = 10, validators=[alphanumeric])
    city = models.CharField(max_length = 255)
    house = models.CharField(max_length = 255)
    photo = models.ImageField(null = True, upload_to = customer_photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Account(models.Model):
    balance = models.DecimalField(default = 0, max_digits = 12, decimal_places = 2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT) #we cann't delete if it have a balance


class Action(models.Model):
    amount = models.DecimalField(max_digits = 12, decimal_places = 2)
    date = models.DateTimeField(auto_now_add = True)
    account = models.ForeignKey(Account, on_delete = models.CASCADE, related_name = 'actions')

    def __str__(self):
            return f'Account number {self.account.id} was changed on {str(self.amount)}'
