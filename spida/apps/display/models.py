from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.

class Suppliers(models.Model):
    username = models.CharField(max_length=30)
    price = models.LargeInterField()
    description = models.TextField(max_length=400)
    date = models.DateTimeField()
    image_item = models.ImageField(upload="")
    logo = models.ImageField(upload="")

    class Meta:
        abstruct = True

@python_2_unicode_compatible
class Supplier(Suppliers):

    def __unicode__(self):
        return "{}'s' profile". format(self.username)
