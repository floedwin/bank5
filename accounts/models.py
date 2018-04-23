from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
    post = models.CharField(max_length=200)
    user = models.ForeignKey(User)

class Registercustomer(models.Model):
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    email = models.EmailField(blank=True)
    contact = models.IntegerField(default=0)
    residence = models.CharField(max_length=200, default='')
    occupation = models.CharField(max_length=200, default='')
    next_of_kin = models.CharField(max_length=200, default='')
    relationship = models.CharField(max_length=200, default='')



    def __str__(self):
        return self.first_name

class CustomerBankaccount(models.Model):
    full_name = models.CharField(max_length=200, default='')
    email = models.EmailField(blank=True)
    contact = models.IntegerField(default=0)
    residence = models.CharField(max_length=200, default='')
    work_history = models.CharField(max_length=200, default='')
    identification_information = models.IntegerField(default=0)
    next_of_kin = models.CharField(max_length=200, default='')
    relationship = models.CharField(max_length=200, default='')
    account_number = models.IntegerField(default=0)
    def __str__(self):
        return self.full_name

class Registercustomertranscations(models.Model):
    Full_name = models.CharField(max_length=200, default='')
    Email = models.EmailField(blank=True)
    Contact = models.IntegerField(default=0)
    Account_number = models.IntegerField(default=0)
    Transcation_type = models.CharField(max_length=200, default='')
    Amount = models.IntegerField(default=0)
    Transcation_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.Full_name


def __unicode__(self):
    return self.first_name




