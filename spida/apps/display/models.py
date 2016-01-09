from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.

class Suppliers(models.Model):
    brand_name = models.CharField(max_length=30)
    email = models.EmailFeld() 
    price = models.IntegerField()
    description = models.TextField(max_length=400)
    date = models.DateTimeField()
    image = models.ImageField()
    logo = models.ImageField()

    class Meta:
        abstract = True

# @python_2_unicode_compatible
class Supplier(Suppliers):

    def __unicode__(self):
        return "{}'s' profile". format(self.username)
